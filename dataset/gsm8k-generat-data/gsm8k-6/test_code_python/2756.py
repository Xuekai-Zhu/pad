def solution():
    # Calculate the total number of stores opened in 2019 and 2020
    stores_opened = 5 + 10

    # Calculate the total number of stores closed in 2019 and 2020
    stores_closed = 2 + 6

    # Calculate the total number of stores at the end of 2020
    total_stores = 23 + stores_opened - stores_closed
    result = total_stores
    return result

print(solution())