from numpy import mean
import generate_data as gd
SORT_METHODS = ["ratio", "profit", "dd_asc", "time_desc", "time_asc"]

def calculate_lateness(schedule, pct):
    # input: schedule = list of tuples (time, profit, due_date)
    
    flights = {} # (flight, time completed)
    running_time = 0
    lateness = 0
    total_profit = 0
    max_profit = sum([i[1] for i in schedule])
    for flight in schedule:
        time = flight[0]
        profit = flight[1]
        due_date = flight[2]
        running_time += time
        flights[flight] = running_time
        # if running_time > due_date:
        #     diff = running_time - due_date
        #     lateness += diff
        #     # print('profit: ', profit)
        #     # print('time: ', time)
        #     # print('diff: ', diff)
        #     # print('min: ', time * pct * diff)
        #     profit -= time * pct * diff
        #     # print('profit - min: ', profit)
        # total_profit += profit

    for flight in flights.keys():
        time = flight[0]
        profit = flight[1]
        due_date = flight[2]
        if due_date < flights[flight]:
            diff = flights[flight] - due_date
            profit -= time * pct * diff
            total_profit += profit

    return total_profit, total_profit/max_profit, max_profit - total_profit, lateness, lateness/running_time

        

def sort_data(data, sort_method):
    if sort_method == "ratio":
        return sorted(data, key=lambda x: (x[0]/x[1]))
    if sort_method == "profit":
        return sorted(data, key=lambda x: x[1], reverse=True)
    if sort_method == "dd_asc":
        return sorted(data, key=lambda x: x[2])
    if sort_method == "time_desc":
        return sorted(data, key=lambda x: x[0], reverse=True)
    if sort_method == "time_asc":
        return sorted(data, key=lambda x: x[0])

def schedule(n):
    data_random = gd.generate_random(n)
    data_maj_long = gd.generate_maj_long(n)
    data_maj_short = gd.generate_maj_short(n)
    data_one_long = gd.generate_one_long(n)
    data_increase_log = gd.generate_money_increase_log(n)
    data_increase_sqrt = gd.generate_money_increase_sqrt(n)
    data = sort_data(data_random, 'dd_asc')
    total_sum = 0
    for i in data:
        total_sum += i[1]
    print(total_sum)
    profits = []
    for i in range(1000):
        data = sort_data(gd.generate_random(n), 'time_asc')
        profits.append(calculate_lateness(data, .02))
    
    num_pos = 0
    for i in profits:
        if i > 0:
            num_pos += 1
    
    print(num_pos/len(profits))

def schedule_random(n):
    total_profits = [] 
    profit_ratios = []
    profit_diffs = []
    lateness_list = []
    lateness_ratios = []
    for method in SORT_METHODS:
        for _ in range(1000):
            data = sort_data(gd.generate_random(n), method)
            total_profit, profit_ratio, profit_diff, lateness, lateness_ratio = calculate_lateness(data, .0001)
            total_profits.append(total_profit)
            profit_ratios.append(profit_ratio)
            profit_diffs.append(profit_diff)
            lateness_list.append(lateness)
            lateness_ratios.append(lateness_ratio)

        print("%s Report: "%method.upper())
        print("Average Profit: ", mean(total_profits))
        print("Average (Profit / Max Profit): ", mean(profit_ratios))
        print("Average (Profit - Max Profit): ", mean(profit_diffs))
        print("Average Lateness: ", mean(lateness_list))
        print("Average (Lateness / Sum Of Flight Times): ",mean(lateness_ratios))
    
    

            

def schedule_maj_long(n):
    x = 0

def schedule_maj_short(n):
    x = 0
    
def schedule_one_long(n):
    x = 0

def schedule_increase_log(n):
    x = 0
    
def schedule_increase_sqrt(n):
    x = 0

if __name__ == "__main__":
    schedule_random(100)