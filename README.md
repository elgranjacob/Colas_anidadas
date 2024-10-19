# Colas_anidadas
El sistema gestiona pedidos de clientes, permitiendo encolar (agregar) y desencolar (atender) pedidos.

Características
Order: Clase que representa un pedido con atributos de cliente y cantidad. Incluye un método para imprimir los detalles del pedido.

QueueInterface: Interfaz base que define los métodos esenciales de una cola (tamaño, si está vacía, frente, encolar y desencolar).

OrderQueue: Implementación de QueueInterface utilizando una lista en Python para manejar los elementos de la cola.

Funcionalidades
Encotar Pedido: Permite agregar un pedido a la cola de pedidos.

Desencotar Pedido: Permite atender (remover) el primer pedido de la cola.

Verificar Tamaño y Estado: Verifica el tamaño de la cola y si está vacía.

Mostrar Primer Elemento: Muestra el primer pedido en la cola sin eliminarlo.
