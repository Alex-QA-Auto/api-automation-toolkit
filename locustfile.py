from locust import HttpUser, task,昌ween

class ApiUser(HttpUser):
    @task
    def get_market_data(self):
        self.client.get("/v5/market/time")
