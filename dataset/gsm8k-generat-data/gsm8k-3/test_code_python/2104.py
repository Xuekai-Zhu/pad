def solution():
    """Bill is making omelets for his family's breakfast. It takes him 3 minutes to chop a pepper, 4 minutes to chop an onion, and 1 minute to grate enough cheese for one omelet. It takes him 5 minutes to assemble and cook the omelet. If he needs to chop up four peppers, two onions, and also grates cheese for cooking each of five omelets, how long will he spend preparing for and cooking the five omelets?"""
    # Define the time it takes to complete each task
    pepper_time = 3
    onion_time = 4
    cheese_time = 1
    omelet_time = 5

    # Define the number of each item needed
    num_peppers = 4
    num_onions = 2
    num_omelets = 5

    # Calculate the total time to prepare the ingredients
    prep_time = (num_peppers * pepper_time) + (num_onions * onion_time) + (num_omelets * cheese_time)

    # Calculate the total time to cook the omelets
    cook_time = num_omelets * omelet_time

    # Calculate the total time to prepare and cook the omelets
    total_time = prep_time + cook_time

    # Display the total time
    result = total_time
    return result

print(solution())