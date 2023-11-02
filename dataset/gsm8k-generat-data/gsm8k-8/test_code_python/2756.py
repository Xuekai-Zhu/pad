def solution():
    # Starting number of stores
    stores = 23

    # 2019 - Opened 5 stores, closed 2 worst-performing
    stores += 5 - 2

    # 2020 - Opened 10 stores, closed 6 worst-performing
    stores += 10 - 6

    result = stores
    return result

print(solution())