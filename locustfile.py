from locust import HttpUser, task, between, constant

class MyUser(HttpUser):
    wait_time = constant(1)  # You can adjust the wait time between requests

    @task
    def send_message(self):
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "sender": "user",
            "message": "NV_sir"
        }
        response = self.client.post("http://127.0.0.1:5005/webhooks/rest/webhook", json=payload, headers=headers)

        # Uncomment the line below to see the response in the Locust console
        # print(response.text)
