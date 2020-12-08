from random import random

from src.distribution import ber, exponential, mean, rand
from src.simulation import Client, Simulation

total_simulations = 1000
arrive_rush_time = 4
arrive_normal_time = 8


def arrive_time(t: int) -> float:
    # from 11:30am to 1:30pm and 5:00pm to 7:00pm, all in minutes
    exp = exponential(5)
    if (90 < t < 210) or (420 < t < 540):
        return exp * arrive_rush_time  # rush time!!
    else:
        return exp * arrive_normal_time  # normal time


def request_selection() -> int:
    return int(ber(0.5))


def request_cook_time(type: int) -> float:
    if type == 0:
        return rand(3, 5)  # sandwich
    else:
        return rand(5, 8)  # sushi


def total_empoyes(t: int):
    if (90 < t < 210) or (420 < t < 540):
        return 2  # rush time!!
    else:
        return 2


total_clientes = []
total_fails = []
total_mean = []

for _ in range(total_simulations):
    simulation = Simulation(
        duration=660,
        get_client_arrive=arrive_time,
        get_client_request=request_selection,
        get_request_minutes=request_cook_time,
        get_total_employes=total_empoyes,
    )
    simulation.start()
    times = [c.recived_time - c.arrive_time for c in simulation.all_clients]

    fails = list(
        filter(
            lambda client: client.recived_time - client.arrive_time > 5,
            simulation.all_clients,
        )
    )
    total_clientes.append(len(simulation.all_clients))
    total_fails.append(len(fails))
    total_mean.append(mean(times))

print(f"total: {mean(total_clientes)}")
print(f"fails: {mean(total_fails)}")
print(f"mean: {mean(total_mean)}")
