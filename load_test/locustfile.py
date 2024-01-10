from locust import HttpUser, TaskSet, task,between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_data(self):
        self.client.get("/")
       