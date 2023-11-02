def solution():
    # Calculate the number of customers a salon has each day
    cans_per_customer = 2  # each customer needs 1 can of hairspray during styling and 1 can to take home
    extra_cans = 5  # the salon buys an extra 5 cans of hairspray each day
    total_cans = 33  # the salon buys 33 cans of hairspray every day
    customers_per_day = (total_cans - extra_cans) / cans_per_customer
    result = customers_per_day
    return result

print(solution())