def solution():
    # Calculate the amount of soda Danny has left
    remaining_soda = (1-0.9)*1 + (1-0.7)*2*0.3  # Danny drinks 90% of one bottle, gives 70% of the other two to his friends, and keeps the rest
    percentage_soda_left = remaining_soda * 100  # express remaining soda as a percentage of a full bottle
    result = percentage_soda_left
    return result

print(solution())