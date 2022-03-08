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
        t = random.randint(400, 900)
        p = random.uniform(.8, 2.0)*t
        f = Flight(t, p)
        schedule.append(f)
    
    for _ in range(n_min):
        t = random.randint(60, 200)
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
        t = random.randint(400, 900)
        p = random.uniform(.8, 2.0)*t
        f = Flight(t, p)
        schedule.append(f)
    
    for _ in range(n_maj):
        t = random.randint(60, 200)
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

def generate_money_increase_exp(n):
    schedule = []
    due_date_set = set()

    for _ in range(n):
        t = random.randint(60, 900)
        p = random.uniform(.95, 1.05) * math.exp(t/100)
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
    schedule = generate_random(n-1)
    total_time = sum([i.time for i in schedule])
    # Create one long flight and attributes

    t = random.randint(total_time // 2, total_time)
    p = random.uniform(.8, 2.0) * t
    long_flight = Flight(t, p)
    
    # Generate random due date of long flight now that we have all flight data
    due_date_set = set([i.due_date for i in schedule])
    d = random.randint(0, total_time)
    while d < long_flight.time or d in due_date_set:
        d = random.randint(0, total_time)
    long_flight.set_due_date(d)
    schedule.append(long_flight)

    return schedule

def generate_money_increase_log(n):
    schedule = []
    due_date_set = set()

    for i in range(n):
        t = random.randint(60,900)
        p = math.log(t) * random.uniform(.95, 1.05) * 100
        schedule.append(Flight(t, p))

    sum_time = sum([i.time for i in schedule])
    for flight in schedule:
        d = random.randint(0, sum_time)
        while d < flight.time or d in due_date_set:
            d = random.randint(0, sum_time)
        flight.set_due_date(d)
        due_date_set.add(d)

    return schedule

def generate_money_increase_sqrt(n):
    schedule = []
    due_date_set = set()

    for i in range(n):
        t = random.randint(60,900)
        p = math.sqrt(t) * random.uniform(.95, 1.05) * 15
        schedule.append(Flight(t, p))

    sum_time = sum([i.time for i in schedule])
    for flight in schedule:
        d = random.randint(0, sum_time)
        while d < flight.time or d in due_date_set:
            d = random.randint(0, sum_time)
        flight.set_due_date(d)
        due_date_set.add(d)

    return schedule

def generate_long_and_short_due_dates(n):
    schedule = []
    due_date_set = set()

    for _ in range(n):
        t = random.randint(60, 900)
        p = random.uniform(.8, 2.0)*t
        f = Flight(t, p)
        schedule.append(f)

    sum_time = sum([i.time for i in schedule])
    schedule_short = schedule[0:len(schedule)//2]
    schedule_long = schedule[len(schedule)//2:len(schedule)]
    for flight in schedule_short:
        d = random.randint(0, sum_time // 10)
        while d < flight.time or d in due_date_set:
            d = random.randint(0, sum_time)
        flight.set_due_date(d)
        due_date_set.add(d)

    for flight in schedule_long:
        d = random.randint(int(.9 * sum_time), sum_time)
        while d < flight.time or d in due_date_set:
            d = random.randint(0, sum_time)
        flight.set_due_date(d)
        due_date_set.add(d)

    return schedule

def get_data_sets(n):
    data =[
        (generate_random(n), "Random"),
        (generate_maj_long(n), "Majority Long"),
        (generate_maj_short(n), "Majority Short"),
        (generate_one_long(n), "One Long"),
        (generate_money_increase_log(n), "Profit follows log(t)"),
        (generate_money_increase_sqrt(n), "Profit follows sqrt(t)"),
        (generate_money_increase_exp(n), "Profit follows exp(t)"),
        (generate_long_and_short_due_dates(n), "Long and Short Due Dates")
    ]
    return data
