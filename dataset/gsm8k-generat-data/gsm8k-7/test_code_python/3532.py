def solution():
    num_sandwiches = 20
    
    # Each sandwich is cut in half twice, making 4 portions per sandwich
    num_portions_per_sandwich = 4
    
    total_portions = num_sandwiches * num_portions_per_sandwich
    
    # Each person gets 8 portions, so the number of people that can be fed is the total portions divided by 8
    num_people = total_portions / 8
    
    result = num_people
    return result

print(solution())