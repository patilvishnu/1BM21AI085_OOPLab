import threading
import time
import random
from queue import Queue

class VegetableMarket:
    def __init__(self, capacity):
        self.capacity = capacity
        self.market_queue = Queue(maxsize=capacity)
        self.vegetables = ['Tomato', 'Carrot', 'Cucumber', 'Lettuce']
        self.producer_threads = []
        self.consumer_threads = []
        self.lock = threading.Lock()
        self.is_simulation_running = True

    def farmer_producer(self, farmer_id):
        while self.is_simulation_running:
            time.sleep(random.uniform(1, 3))
            vegetable = random.choice(self.vegetables)
            with self.lock:
                if self.market_queue.full():
                    print(f"Farmer {farmer_id} is waiting. Market is full.")
                else:
                    self.market_queue.put(vegetable)
                    print(f"Farmer {farmer_id} produced {vegetable}. Market: {list(self.market_queue.queue)}")

    def consumer_buyer(self, buyer_id):
        while self.is_simulation_running:
            time.sleep(random.uniform(2, 5))
            with self.lock:
                if not self.market_queue.empty():
                    vegetable = self.market_queue.get()
                    print(f"Buyer {buyer_id} purchased {vegetable}. Market: {list(self.market_queue.queue)}")
                else:
                    print(f"Buyer {buyer_id} is waiting. No vegetables available.")

    def stop_simulation(self):
        self.is_simulation_running = False

    def run_market_simulation(self, num_producers, num_consumers):
        for i in range(num_producers):
            producer_thread = threading.Thread(target=self.farmer_producer, args=(i + 1,))
            self.producer_threads.append(producer_thread)
            producer_thread.start()

        for i in range(num_consumers):
            consumer_thread = threading.Thread(target=self.consumer_buyer, args=(i + 1,))
            self.consumer_threads.append(consumer_thread)
            consumer_thread.start()

        
        time.sleep(5)

        
        self.stop_simulation()

        for producer_thread in self.producer_threads:
            producer_thread.join()

        for consumer_thread in self.consumer_threads:
            consumer_thread.join()

if __name__ == "__main__":
    market = VegetableMarket(capacity=5)
    market.run_market_simulation(num_producers=3, num_consumers=5)
