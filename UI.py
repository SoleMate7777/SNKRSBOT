import tkinter as tk


class SNKRSBotGUI:

    def __init__(self):
        # Create the main window
        self.root = tk.Tk()

        # Create the proxies label
        self.proxies_label = tk.Label(self.root, text="Proxies")

        # Create the proxies entry
        self.proxies_entry = tk.Entry(self.root)

        # Create the profiles label
        self.profiles_label = tk.Label(self.root, text="Profiles")

        # Create the profiles entry
        self.profiles_entry = tk.Entry(self.root)

        # Create the tasks label
        self.tasks_label = tk.Label(self.root, text="Tasks")

        # Create the tasks entry
        self.tasks_entry = tk.Entry(self.root)

        # Create the accounts label
        self.accounts_label = tk.Label(self.root, text="Accounts")

        # Create the accounts entry
        self.accounts_entry = tk.Entry(self.root)

        # Create the start button
        self.start_button = tk.Button(self.root, text="Start", command=self.start_bot)

        # Layout the widgets
        self.proxies_label.grid(row=0, column=0)
        self.proxies_entry.grid(row=0, column=1)
        self.profiles_label.grid(row=1, column=0)
        self.profiles_entry.grid(row=1, column=1)
        self.tasks_label.grid(row=2, column=0)
        self.tasks_entry.grid(row=2, column=1)
        self.accounts_label.grid(row=3, column=0)
        self.accounts_entry.grid(row=3, column=1)
        self.start_button.grid(row=4, column=0)

        # Start the main loop
        self.root.mainloop()

    def start_bot(self):
        # Get the proxies, profiles, tasks, and accounts from the user
        proxies = self.proxies_entry.get().split(",")
        profiles = self.profiles_entry.get().split(",")
        tasks = self.tasks_entry.get().split(",")
        accounts = self.accounts_entry.get().split(",")

        # Create a SNKRS bot with the specified proxies, profiles, tasks, and accounts
        bot = SNKRSBot(proxies, profiles, tasks, accounts)

        # Start the bot
        bot.start()


if __name__ == "__main__":
    # Create a SNKRS bot GUI
    gui = SNKRSBotGUI()