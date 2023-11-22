def solution():
    
    # Define the number of people and the required weight per sandwich
    NUM_PEOPLE = 20
    REQUIRED_WEIGHT_PER_SANDWICH = 1

    # Calculate the total weight of sandwiches required
    total_weight = NUM_PEOPLE * REQUIRED_WEIGHT_PER_SANDWICH

    # Calculate the cost of the meat and cheese
    meat_cost = total_weight * 7
    cheese_cost = total_weight * 3

    # Calculate the total cost of the meat and cheese
    total_cost = meat_cost + cheese_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())