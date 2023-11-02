def solution():
    num_passengers = 4
    orange_cost = 1.5
    snack_cost = 15
    
    # Calculate the total number of oranges received
    total_oranges = num_passengers
    
    # Calculate the cost of the oranges they would have bought at the stop
    oranges_saved = total_oranges * orange_cost
    
    # Calculate the percentage of money saved by not buying oranges at the stop
    percentage_saved = (oranges_saved / snack_cost) * 100
    result = percentage_saved
    return result

print(solution())