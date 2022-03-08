from numpy import mean
from generate_data import get_data_sets
from report import Report
from reportset import ReportSet

def calculate_lateness(schedule, pct):
    # input: schedule = list of tuples (time, profit, due_date)
    running_time = 0
    lateness = 0
    total_profit = 0
    max_profit = sum([i.profit for i in schedule])
    for flight in schedule:
        running_time += flight.time
        flight.set_landing_time(running_time)

    for flight in schedule:
        lateness += flight.lateness
        profit = flight.profit
        profit -= flight.time * pct * flight.lateness
        total_profit += profit

    return [total_profit, total_profit/max_profit, max_profit - total_profit, lateness, lateness/running_time]

        

def sort_data(data, sort_method):
    if sort_method == "time_money_ratio_asc":
        return sorted(data, key=lambda x: (x.time/x.profit))
    if sort_method == "profit":
        return sorted(data, key=lambda x: x.profit, reverse=True)
    if sort_method == "dd_asc":
        return sorted(data, key=lambda x: x.due_date)
    if sort_method == "time_desc":
        return sorted(data, key=lambda x: x.time, reverse=True)
    if sort_method == "time_asc":
        return sorted(data, key=lambda x: x.time)
    if sort_method == "urgency":
        return sorted(data, key=lambda x: x.profit/x.due_date, reverse=True)

def schedule(data, name, pct):
    sort_methods = ["time_money_ratio_asc", "profit", "dd_asc", "time_desc", "time_asc", "urgent"]
    total_profits = [] 
    profit_ratios = []
    profit_diffs = []
    lateness_list = []
    lateness_ratios = []
    for method in sort_methods:
        data = sort_data(data, method)
        total_profit, profit_ratio, profit_diff, lateness, lateness_ratio = calculate_lateness(data, pct)
        total_profits.append(total_profit)
        profit_ratios.append(profit_ratio)
        profit_diffs.append(profit_diff)
        lateness_list.append(lateness)
        lateness_ratios.append(lateness_ratio)

        print("%s Sorting Report With %s Data: "%(method.title(), name))
        print("Average Profit: ", mean(total_profits))
        print("Average (Profit / Max Profit): ", mean(profit_ratios))
        print("Average (Max Profit - Profit): ", mean(profit_diffs))
        print("Average Lateness: ", mean(lateness_list))
        print("Average (Lateness / Sum Of Flight Times): ",mean(lateness_ratios))

def print_report(n, pct):
    sort_methods = ["time_money_ratio_asc", "profit", "dd_asc", "time_desc", "time_asc", "urgency"]
    data_sets = ["random", "maj_long", "maj_short", "one_long", "money_increase_log", "money_increase_sqrt", "money_increase_exp", "long_and_short_dd"]
    avgs = {}
    for i in data_sets:
        avgs[i] = {}
        for method in sort_methods:
            avgs[i][method] = Report(i, method)

    for _ in range(1000):
        data = get_data_sets(n)
        for i, data_set in enumerate(data):
            for method in sort_methods:
                sorted_data = sort_data(data_set[0], method)
                report = calculate_lateness(sorted_data, pct)
                avgs[data_sets[i]][method].add_report(report)

    for i in data_sets:
        rs = ReportSet()
        for method in sort_methods:
            report = avgs[i][method]
            rs.add_report(report)
            report.print_report()
        rs.print_stats()
        print()

            