import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SNKRSBot:

    def __init__(self, proxies, profiles, tasks, accounts):
        self.proxies = proxies
        self.profiles = profiles
        self.tasks = tasks
        self.accounts = accounts

        # Create a Chrome driver with the specified proxies
        self.driver = webdriver.Chrome(options=Options(), proxies=proxies)

        # Navigate to the SNKRS website
        self.driver.get("https://www.nike.com/launch/")

        # Login to each account
        for account in self.accounts:
            self.login(account)

        # Start executing tasks
        for task in self.tasks:
            self.execute_task(task)

    def login(self, account):
        # Find the username and password fields
        username_field = self.driver.find_element_by_id("username")
        password_field = self.driver.find_element_by_id("password")

        # Enter the username and password
        username_field.send_keys(account["username"])
        password_field.send_keys(account["password"])

        # Click the login button
        login_button = self.driver.find_element_by_id("login")
        login_button.click()

    def execute_task(self, task):
        # Find the product page for the desired sneaker
        product_page = self.driver.find_element_by_id(task["product_id"])

        # Add the sneaker to the cart
        product_page.click()

        # Check out
        self.driver.find_element_by_id("checkout").click()

        # Enter shipping and billing information
        self.driver.find_element_by_id("shipping_address").send_keys(task["shipping_address"])
        self.driver.find_element_by_id("billing_address").send_keys(task["billing_address"])

        # Select a payment method
        self.driver.find_element_by_id("payment_method").click()

        # Submit the order
        self.driver.find_element_by_id("submit_order").click()


class RequestBase:

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def make_request(self):
        response = requests.get(self.url, headers=self.headers)
        return response


class SNKRSRequest(RequestBase):

    def __init__(self, url, headers, product_id, account):
        super().__init__(url, headers)
        self.product_id = product_id
        self.account = account

    def make_request(self):
        response = super().make_request()
        if response.status_code == 200:
            # The request was successful
            return response
        else:
            # The request failed
            return None


if __name__ == "__main__":
    # Get the proxies, profiles, tasks, and accounts from the user
    proxies = input("Enter the proxies, separated by commas: ").split(",")
    profiles = input("Enter the profiles, separated by commas: ").split(",")
    tasks = input("Enter the tasks, separated by commas: ").split(",")
    accounts = input("Enter the accounts, separated by commas: ").split(",")

    # Create a SNKRS bot with the specified proxies, profiles, tasks, and accounts
    bot = SNKRSBot(proxies, profiles, tasks, accounts)

    # Start the bot
    bot.start()
