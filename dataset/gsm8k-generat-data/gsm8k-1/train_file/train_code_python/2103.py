def solution():
    """Bill is making omelets for his family's breakfast. It takes him 3 minutes to chop a pepper, 4 minutes to chop an onion, and 1 minute to grate enough cheese for one omelet. It takes him 5 minutes to assemble and cook the omelet. If he needs to chop up four peppers, two onions, and also grates cheese for cooking each of five omelets, how long will he spend preparing for and cooking the five omelets?"""
    pepper_time = 3
    onion_time = 4
    cheese_time = 1
    omelet_time = 5
    total_time = (pepper_time * 4) + (onion_time * 2) + (cheese_time * 5) + (omelet_time * 5)
    result = total_time
    return result

print(solution())