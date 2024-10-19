class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print_order(self):
        print(f"     Customer: {self.customer}")
        print(f"     Quantity: {self.qtty}")
        print("     ------------")

class QueueInterface:
    def size(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def front(self):
        raise NotImplementedError

    def enqueue(self, info):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

class OrderQueue(QueueInterface):
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def front(self):
        return self.queue[0] if not self.is_empty() else None

    def enqueue(self, info):
        self.queue.append(info)

    def dequeue(self):
        return self.queue.pop(0) if not self.is_empty() else None

def main():
    order_queue = OrderQueue()

    
    order1 = Order(5, "Cliente A")
    order2 = Order(3, "Cliente B")
    order_queue.enqueue(order1)
    order_queue.enqueue(order2)

    
    print("Tamaño de la cola:", order_queue.size())
    print("Frente de la cola:")
    front_order = order_queue.front()
    if front_order:
        front_order.print_order()

    
    print("Atendiendo un pedido:")
    served_order = order_queue.dequeue()
    if served_order:
        served_order.print_order()

   
    print("Tamaño de la cola después de atender:", order_queue.size())

if __name__ == "__main__":
    main()
