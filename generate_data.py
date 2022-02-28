import random

def generate_random(n):
    time = []
    profit = []
    for _ in range(n):
        t = random.randint(15, 120)
        time.append(t)
        profit.append(random.uniform(.8, 2.0)*t)
    return zip(time, profit)

def generate_maj_long(n):
    n_maj = int(.8*n)
    n_min = n - n_maj

    time = []
    profit = []
    
    for _ in range(n_maj):
        t = random.randint(45, 120)
        time.append(t)
        profit.append(random.uniform(.8, 2.0)*t)

    for _ in range(n_min):
        t = random.randint(15, 30)
        time.append(t)
        profit.append(random.uniform(.8, 2.0)*t)

    random.shuffle(time)
    random.shuffle(profit)

    return zip(time, profit)

def generate_maj_short(n):
    n_maj = int(.8*n)
    n_min = n - n_maj

    time = []
    profit = []
    
    for _ in range(n_maj):
        t = random.randint(15, 30)
        time.append(t)
        profit.append(random.uniform(.8, 2.0)*t)

    for _ in range(n_min):
        t = random.randint(45, 120)
        time.append(t)
        profit.append(random.uniform(.8, 2.0)*t)


    random.shuffle(time)
    random.shuffle(profit)

    return zip(time, profit)

def generate_one_long(n):
    # TODO
    x = 0

def generate_money_increase_log(n):
    # TODO
    x = 0

def generate_money_increase_sqrt(n):
    # TODO
    x = 0