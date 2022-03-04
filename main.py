import generate_data as gd

def calculate_lateness(schedule):
    # input: schedule = list of tuples (time, profit, due_date)
    x = 0
    for flight in schedule:
        x = 0

def sort_data(data, sort_method):
    if sort_method == "ratio":
        return sorted(data, key=lambda x: (x[0]/x[1]))
    if sort_method == "profit":
        return sorted(data, key=lambda x: x[1], reverse=True)
    if sort_method == "dd_asc":
        return sorted(data, lambda x: x[2])
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
    
    
    


if __name__ == "__main__":
    print('hello world')
    schedule(10)