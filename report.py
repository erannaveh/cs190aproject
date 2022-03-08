from numpy import mean
class Report:
    def __init__(self, data_set, method):
        self.data_set = data_set
        self.method = method
        self.total_profit = []
        self.profit_ratio = []
        self.profit_diff = []
        self.lateness = []
        self.lateness_ratio = []
    
    def add_report(self, report):
        self.total_profit.append(report[0])
        self.profit_ratio.append(report[1])
        self.profit_diff.append(report[2])
        self.lateness.append(report[3])
        self.lateness_ratio.append(report[4])
    
    def calc_avgs(self):
        self.average_profit = mean(self.total_profit)
        self.average_profit_ratio = mean(self.profit_ratio)
        self.average_profit_diff = mean(self.profit_diff)
        self.average_lateness = mean(self.lateness)
        self.average_lateness_ratio = mean(self.lateness_ratio)

    def print_report(self):
        self.calc_avgs()
        print("%s Sorting Report With %s Data: "%(self.method.title(), self.data_set.title()),)
        print("Average Profit: ", self.average_profit)
        print("Average (Profit / Max Profit): ", self.average_profit_ratio)
        print("Average (Max Profit - Profit): ", self.average_profit_diff)
        print("Average Lateness: ", self.average_lateness)
        print("Average (Lateness / Sum Of Flight Times): ", self.average_lateness_ratio)