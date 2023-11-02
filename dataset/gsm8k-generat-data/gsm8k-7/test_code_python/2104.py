def solution():
    peppers = 4
    onions = 2
    cheese = 5
    pepper_time = 3
    onion_time = 4
    cheese_time = 1
    cook_time = 5

    # Calculate the total time spent chopping peppers
    total_pepper_time = peppers * pepper_time

    # Calculate the total time spent chopping onions
    total_onion_time = onions * onion_time

    # Calculate the total time spent grating cheese
    total_cheese_time = cheese * cheese_time

    # Calculate the total time spent cooking
    total_cook_time = cook_time * cheese

    # Calculate the total time spent preparing for and cooking the omelets
    total_time = total_pepper_time + total_onion_time + total_cheese_time + total_cook_time
    result = total_time
    return result

print(solution())