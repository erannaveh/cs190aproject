import random
import math

# def generate_random(n):
#     time = []
#     profit = []
#     for _ in range(n):
#         t = random.randint(15, 120)
#         time.append(t)
#         profit.append(random.uniform(.8, 2.0)*t)
#     return zip(time, profit)

def generate_random(n):
    due_date = set()
    time = []
    profit = []
    for _ in range(n):
        t = random.randint(60, 900)
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
    # TODO
    x = 0

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

data = generate_money_increase_log(10)
print(data)
