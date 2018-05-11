from kombu import Exchange, Queue

# creating direct exchange for rabbitmq
exchange = Exchange('pathao-food', type='direct')

# declaring queue list
order_queue = Queue(name='order-queue', exchange=exchange, routing_key='order-queue')
restaurant_queue = Queue(name='restaurant-queue', exchange=exchange, routing_key='restaurant-queue')