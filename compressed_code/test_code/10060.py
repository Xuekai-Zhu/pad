def solution():
    
    initial_collection = 40
    percent_increase = 20
    increase_amount = initial_collection * (percent_increase / 100)
    total_collection = initial_collection + increase_amount
    result = total_collection
    return result

print(solution())