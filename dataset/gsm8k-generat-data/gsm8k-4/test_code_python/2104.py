def solution():
    """Bill is making omelets for his family's breakfast. It takes him 3 minutes to chop a pepper, 4 minutes to chop an onion, and 1 minute to grate enough cheese for one omelet. It takes him 5 minutes to assemble and cook the omelet. If he needs to chop up four peppers, two onions, and also grates cheese for cooking each of five omelets, how long will he spend preparing for and cooking the five omelets?"""
    # Define the time it takes to chop a pepper, onion, and grate cheese
    pepper_time = 3
    onion_time = 4
    cheese_time = 1

    # Define the time it takes to cook one omelet
    cook_time = 5

    # Define the number of peppers, onions, and omelets needed
    num_peppers = 4
    num_onions = 2
    num_omelets = 5

    # Calculate the total time to chop the peppers
    pepper_total_time = num_peppers * pepper_time

    # Calculate the total time to chop the onions
    onion_total_time = num_onions * onion_time

    # Calculate the total time to grate cheese for all the omelets
    cheese_total_time = num_omelets * cheese_time

    # Calculate the total time to cook all the omelets
    cook_total_time = num_omelets * cook_time

    # Calculate the total time spend preparing for and cooking the omelets
    total_time = pepper_total_time + onion_total_time + cheese_total_time + cook_total_time

    result = total_time
    return result

print(solution())