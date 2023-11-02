def solution():
    """Chester must deliver ten bales of hay to Farmer Brown. Farmer Brown wants Chester to supply better quality hay and double the delivery of bales of hay. If the previous hay cost $15 per bale, and the better quality one cost $18 per bale, how much more money will Farmer Brown need to meet his own new requirements?"""
    # Define the number of bales of hay initially required
    initial_bales = 10

    # Calculate the cost of the initial hay delivery
    initial_cost = initial_bales * 15

    # Calculate the number of bales of better quality hay required
    new_bales = initial_bales * 2

    # Calculate the cost of the new hay delivery
    new_cost = new_bales * 18

    # Calculate the difference in cost
    cost_difference = new_cost - initial_cost

    # return the result
    result = cost_difference
    return result

print(solution())