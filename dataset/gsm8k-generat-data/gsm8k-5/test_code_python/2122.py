def solution():
    cans_per_customer = 2  # Each customer needs 1 can of hairspray during the styling and 1 can to take home
    extra_cans = 5  # The salon buys an extra 5 cans of hairspray each day
    total_cans = 33  # The salon buys a total of 33 cans of hairspray each day

    # Calculate the number of customers
    total_customers = (total_cans - extra_cans) / cans_per_customer
    result = total_customers
    return result

print(solution())