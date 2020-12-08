from math import inf
from typing import Callable

from .distribution import *  # noqa: F403, F401


class Client:
    def __init__(self, arrive_time: float) -> None:
        self.arrive_time = arrive_time
        self.finish_time: float = inf
        self.recived_time: float = -1


class Simulation:
    def __init__(
        self,
        duration: int,
        get_client_arrive: Callable[[int], float],
        get_client_request: Callable[[], int],
        get_request_minutes: Callable[[int], float],
        get_total_employes: Callable[[int], int],
    ) -> None:
        self.duration = duration
        self.get_client_arrive = get_client_arrive
        self.get_client_request = get_client_request
        self.get_request_minutes = get_request_minutes
        self.get_total_employes = get_total_employes

        self.clients: "list[Client]" = []
        self.working_employes = 0
        self.t = 0
        self.all_clients: "list[Client]" = []

    def start(self):

        self.clients.append(Client(self.get_client_arrive(0)))

        while self.t <= self.duration:
            self.t = min(
                [c.arrive_time if c.arrive_time > self.t else inf for c in self.clients]
                + [
                    c.finish_time if c.finish_time > self.t else inf
                    for c in self.clients
                ]
            )
            self.update(self.t)

    def update(self, t):

        if not self.clients:
            return
        if self.clients[0].arrive_time == t:
            self.clients.insert(0, Client(t + self.get_client_arrive(t)))

        for i in range(len(self.clients) - 1, -1, -1):  # from last to first order
            if self.working_employes >= self.get_total_employes(t):
                break
            client = self.clients[i]
            if client.arrive_time <= t and self.clients[i].finish_time == inf:
                self.working_employes += 1

                self.clients[i].finish_time = t + self.get_request_minutes(
                    self.get_client_request()
                )
                client.recived_time = t

        for client in self.clients:
            if client.finish_time == t:
                self.working_employes -= 1
                self.clients.remove(client)
                self.all_clients.append(client)
