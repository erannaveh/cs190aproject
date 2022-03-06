import random

# def generate_random(n):
#     time = []
#     profit = []
#     for _ in range(n):
#         t = random.randint(15, 120)
#         time.append(t)
#         profit.append(random.uniform(.8, 2.0)*t)
#     return zip(time, profit)

def generate_random(n):
    due_date_set = set()
    due_date = []
    time = []
    profit = []
    for _ in range(n):
        t = random.randint(60, 900)
        time.append(t)
        profit.append(random.uniform(.8, 2.0)*t)

    sum_time = sum(time)

    for i in range(n):
        d = random.randint(0, sum_time)
        while d < time[i] or d in due_date_set:
            d = random.randint(0, sum_time)
        due_date.append(d)
        due_date_set.add(d)

    return list(zip(time, profit, due_date))

def generate_maj_long(n):
    n_maj = int(.8*n)
    n_min = n - n_maj

    due_date = set()
    time = []
    profit = []

    for _ in range(n_maj):
        t = random.randint(300, 900)
        time.append(t)
        profit.append(random.uniform(.8, 2.0)*t)
    
    for _ in range(n_min):
        t = random.randint(60, 300)
        time.append(t)
        profit.append(random.uniform(.8, 2.0)*t)

    sum_time = sum(time)
    i = 0
    while len(due_date) < n:
        d = random.randint(0, 2 * sum_time)
        while d < time[i]:
            d = random.randint(0, 2 * sum_time)
        if d not in due_date:
            due_date.add(d)
            i += 1

    return list(zip(time, profit, due_date))

def generate_maj_short(n):
    n_maj = int(.8*n)
    n_min = n - n_maj

    due_date = set()
    time = []
    profit = []

    for _ in range(n_min):
        t = random.randint(300, 900)
        time.append(t)
        profit.append(random.uniform(.8, 2.0)*t)
    
    for _ in range(n_maj):
        t = random.randint(60, 300)
        time.append(t)
        profit.append(random.uniform(.8, 2.0)*t)

    sum_time = sum(time)
    i = 0
    while len(due_date) < n:
        d = random.randint(0, 2 * sum_time)
        while d < time[i]:
            d = random.randint(0, 2 * sum_time)
        if d not in due_date:
            due_date.add(d)
            i += 1

    return list(zip(time, profit, due_date))

def generate_one_long(n):
    # One really long flight, Many short flights 

    # List of randomly generated flight data, size n-1
    flights = generate_random(n-1)

    # Create one long flight and attributes
    long_flight = (0,0,0)

    l = random.randint(300, 900)
    p = random.uniform(.8, 2.0) * l

    long_flight[0] = l
    long_flight[1] = p

    # Add to flights
    flights.append(long_flight)

    # Sum up total times of all flights
    sum_time = 0
    for fl in flights:
        sum_time += fl[0]
    
    # Generate random due date of long flight now that we have all flight data
    d = random.randInt(0, sum_time)

    flights[-1][2] = d

    return flights

def generate_money_increase_log(n):
    new_n = int(n)
    due_date = set()
    time = []
    profit = []

    for i in range(new_n):
        t = random.randint(60,900)
        time.append(t)
        profit.append(math.log(100+t) * random.uniform(.8, 1.2))

    sum_time = sum(time)
    i = 0
    while len(due_date) < n:
        d = random.randint(0, sum_time)
        while d < time[i]:
            d = random.randint(0, sum_time)
        if d not in due_date:
            due_date.add(d)
            i += 1

    return list(zip(time, profit, due_date))

def generate_money_increase_sqrt(n):
    # TODO
    x = 0