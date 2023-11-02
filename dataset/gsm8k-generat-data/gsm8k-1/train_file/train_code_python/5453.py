def solution():
    """Maria collects stamps and wants to enlarge her collection. She has collected 40 stamps so far and plans to have 20\% more. How many stamps in total does Maria want to collect?"""
    initial_collection = 40
    percent_increase = 20
    increase_amount = initial_collection * (percent_increase / 100)
    total_collection = initial_collection + increase_amount
    result = total_collection
    return result

print(solution())