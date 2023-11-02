def solution():
    
    initial_collection = 40
    increase_percent = 20
    desired_increase = initial_collection * (increase_percent / 100)
    total_collection = initial_collection + desired_increase
    result = total_collection
    return result

print(solution())