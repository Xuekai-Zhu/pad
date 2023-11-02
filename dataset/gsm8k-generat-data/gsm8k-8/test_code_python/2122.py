def solution():
    # Subtract the extra 5 cans from the total to find the total number of customer cans used per day
    customer_cans = 33 - 5

    # Divide the customer cans by 2 (since each customer uses 1 can during styling and takes 1 can home)
    customers_per_day = customer_cans / 2
    result = customers_per_day
    return result

print(solution())