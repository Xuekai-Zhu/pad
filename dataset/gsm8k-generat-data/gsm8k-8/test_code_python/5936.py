def solution():
    # Define Harris' flour and amount of cakes
    harris_flour = 400
    num_cakes = 9

    # Calculate the total flour needed for all cakes
    total_flour = 100 * num_cakes * 2  # 2 people baking

    # Calculate Traci's flour by subtracting Harris' from the total needed
    traci_flour = total_flour - harris_flour
    result = traci_flour
    return result

print(solution())