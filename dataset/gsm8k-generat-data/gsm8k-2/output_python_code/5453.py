def solution():
    """Maria collects stamps and wants to enlarge her collection. She has collected 40 stamps so far and plans to have 20% more. How many stamps in total does Maria want to collect?"""
    initial_collection = 40
    increase_percent = 20
    desired_increase = initial_collection * (increase_percent / 100)
    total_collection = initial_collection + desired_increase
    result = total_collection
    return result

print(solution())