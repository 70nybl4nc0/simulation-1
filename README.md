# Informe del Proyecto de Simulación 1

## 1. Orden



### La Cocina de Kojo (Kojo’s Kitchen)

La cocina de Kojo es uno de los puestos de comida rápida en un centro comercial. El centro comercial está abierto entre las 10:00 am y las 9:00 pm cada día. En este lugar se sirven dos tipos de productos: sándwiches y sushi. Para los objetivos de este proyecto se asumirá que existen solo dos tipos de consumidores: unos consumen solo sándwiches y los otros consumen solo productos de la gama del sushi. En Kojo hay dos perı́odos de hora pico durante un día de trabajo; uno entre las 11:30 am y la 1:30 pm, y el otro entre las 5:00 pm y las 7:00 pm. El intervalo de tiempo entre el arribo de un consumidor y el de otro no es homogéneo pero, por conveniencia, se asumirá que es homogéneo. El intervalo de tiempo de los segmentos homogéneos, distribuye de forma exponencial. Actualmente dos empleados trabajan todo el día preparando sándwiches y sushi para los consumidores. El tiempo de preparación depende del producto en cuestión. Estos distribuyen de forma uniforme, en un rango de 3 a 5 minutos para la preparación de sándwiches y entre 5 y 8 minutos para la preparación de sushi.

El administrador de Kojo está muy feliz con el negocio, pero ha estado recibiendo quejas de los consumidores por la demora de sus peticiones. Él está interesado en explorar algunas opciones de distribución del personal para reducir el número de quejas. Su interés está centrado en comparar la situación actual con una opción alternativa donde se emplea un tercer empleado durante los perı́odos más ocupados. La medida del desempeño de estas opciones estará dada por el porciento de consumidores que espera más de 5 minutos por un servicio durante el curso de un día de trabajo.

Se desea obtener el porciento de consumidores que esperan más de 5 minutos cuando solo dos empleados están trabajando y este mismo dato agregando un empleado en las horas pico.

## 2. Modelación del Problema

### Precisiones Iniciales

El problema presentado es equivalente al problema de peticiones a servidores en paralelo, o problema de las colas de petición. 

El tiempo estimado para catalogar como insatisfecho a un cliente es de 5 min, este se contara a partir de que un cliente llega a la cola hasta que es atendido. O sea, si esta mas de 5 min en la cola. Esto lo haremos así porque sino todos los que consuman Sushi no podrían estar satisfechos.

Los clientes no abandonan la cola.

### Modelo de Simulación de Eventos Discretos

El modelo usado para la simulación y resolución del problema es simple. Las variables que mas afectan los resultados son las que definen como distribuye el tiempo de llegada de los nuevos clientes, dentro y fuera del horario pico. Dadas las pruebas se puede notar grandes variaciones en la cantidad de clientes satisfechos.  

Las demás variables están creadas según la orientación del problema.

## 3. Resultados

Los resultados de la simulación revelan un benefician enorme con la introducción del trabajador extra en horas pico, que son las horas donde mas cliente necesitan ser atendidos.

El tiempo entre cliente es homogénea y distribuye exponencial. 

#### Usando máximo de 3 minutos para horarios picos y 8 minutos en horario normal: 

** Para 2 trabajadores fijos:

Promedio de clientes: 162.186
Promedio de fallos: 113.752
Porciento de fallos: 70%
Promedio de minutos por clientes: 17.566728379611515

** Para 2 trabajadores más uno en horarios picos:

Promedio de clientes: 163.719
Promedio de fallos: 2.492
Porciento de fallos: 1.77%
Promedio de minutos por clientes: 0.4008774965134847

#### Usando máximo de 4 minutos para horarios picos y 10 minutos en horario normal: 

**Para 2 trabajadores fijos:

Promedio de clientes: 139.03
Promedio de fallos: 31.64
Porciento de fallos: 22.75%
Promedio de minutos por clientes: 2.93

#** Para 2 trabajadores más uno en horarios picos:

Promedio de clientes: 139.16
Promedio de fallos: 0.53
Porciento de fallos: 0.38%
Promedio de minutos por clientes: 0.08


