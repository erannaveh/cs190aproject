class Flight:
    def __init__(self, time, profit, due_date = 0, landing_time = 0, lateness = 0):
        self.time = time
        self.profit = profit
        self.due_date = due_date
        self.landing_time = landing_time
        self.lateness = lateness

    def set_due_date(self, due_date):
        self.due_date = due_date

    def set_landing_time(self, landing_time):
        self.landing_time = landing_time
        if landing_time > self.due_date:
            self.lateness = landing_time - self.due_date

    def print(self):
        print(self.time, " ", self.profit, " ", self.due_date, " ", self.landing_time, "", self.lateness)