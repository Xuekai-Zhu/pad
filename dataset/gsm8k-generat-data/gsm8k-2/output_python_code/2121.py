def solution():
    """A salon has the same amount of customers every day. Each customer needs 1 can of hairspray during the styling and is also given 1 can of hairspray to take home. The salon also buys an extra 5 cans of hairspray each day to ensure there is never a shortage. If the salon buys 33 cans of hairspray every day, how many customers do they have each day?"""
    total_hairspray = 33
    extra_hairspray = 5
    total_customers = (total_hairspray - extra_hairspray) / 2
    result = total_customers
    return result

print(solution())