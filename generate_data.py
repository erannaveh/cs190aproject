import random
from flight import Flight
import math

def generate_random(n):
    schedule = []
    due_date_set = set()

    for _ in range(n):
        t = random.randint(60, 900)
        p = random.uniform(.8, 2.0)*t
        f = Flight(t, p)
        schedule.append(f)

    sum_time = sum([i.time for i in schedule])

    for flight in schedule:
        d = random.randint(0, sum_time)
        while d < flight.time or d in due_date_set:
            d = random.randint(0, sum_time)
        flight.set_due_date(d)
        due_date_set.add(d)

    return schedule

def generate_maj_long(n):
    schedule = []
    due_date_set = set()
    n_maj = int(.8*n)
    n_min = n - n_maj

    for _ in range(n_maj):
        t = random.randint(300, 900)
        p = random.uniform(.8, 2.0)*t
        f = Flight(t, p)
        schedule.append(f)
    
    for _ in range(n_min):
        t = random.randint(60, 300)
        p = random.uniform(.8, 2.0)*t
        f = Flight(t, p)
        schedule.append(f)

    sum_time = sum([i.time for i in schedule])
    for flight in schedule:
        d = random.randint(0, sum_time)
        while d < flight.time or d in due_date_set:
            d = random.randint(0, sum_time)
        flight.set_due_date(d)
        due_date_set.add(d)

    return schedule

def generate_maj_short(n):
    schedule = []
    due_date_set = set()
    n_maj = int(.8*n)
    n_min = n - n_maj

    for _ in range(n_min):
        t = random.randint(300, 900)
        p = random.uniform(.8, 2.0)*t
        f = Flight(t, p)
        schedule.append(f)
    
    for _ in range(n_maj):
        t = random.randint(60, 300)
        p = random.uniform(.8, 2.0)*t
        f = Flight(t, p)
        schedule.append(f)

    sum_time = sum([i.time for i in schedule])
    for flight in schedule:
        d = random.randint(0, sum_time)
        while d < flight.time or d in due_date_set:
            d = random.randint(0, sum_time)
        flight.set_due_date(d)
        due_date_set.add(d)

    return schedule

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

def get_data_sets(n):
    data =[
        (generate_random(n), "Random"),
        (generate_maj_long(n), "Majority Long"),
        (generate_maj_short(n), "Majority Short")
        # gd.generate_one_long(n),
        # gd.generate_money_increase_log(n),
        # gd.generate_money_increase_sqrt(n),
    ]
    return data