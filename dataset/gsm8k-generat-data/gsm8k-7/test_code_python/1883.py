def solution():
    total_time = 8
    total_gold = 100
    
    # Calculate the amount of gold in each smaller bag
    each_small_bag = total_gold / 2 / 2
    
    # Calculate the total amount of gold found
    total_gold += each_small_bag * 2
    
    # Calculate the amount of gold found per hour
    gold_per_hour = total_gold / total_time
    result = gold_per_hour
    return result

print(solution())