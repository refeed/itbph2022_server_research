import time

from locust import FastHttpUser, constant_throughput, task


class SPBUUser(FastHttpUser):
    # 1 user 1 request per second
    wait_time = constant_throughput(1)

    @task
    def create_transaction(self):
        # Dummy data
        self.client.post(
            "/api/v1/transaction",
            {
                "time": time.time(),
                "buyer_id": "1234567891010",
                "bbm_type": "pertalite",
                "amount_liter": 50,
                "vehicle_id": "AAA12345BBB",
                "spbu_id": "1234123412341234",
            },
            headers={"Content-Type": "application/json"},
        )
