def solution():
    """Chester must deliver ten bales of hay to Farmer Brown. Farmer Brown wants Chester to supply better quality hay and double the delivery of bales of hay. If the previous hay cost $15 per bale, and the better quality one cost $18 per bale, how much more money will Farmer Brown need to meet his own new requirements?"""
    # Define the number of bales of hay and the cost per bale for each type
    num_bales = 10
    old_cost = 15
    new_cost = 18

    # Calculate the cost of the old hay and the new hay
    old_hay_cost = num_bales * old_cost
    new_num_bales = num_bales * 2
    new_hay_cost = new_num_bales * new_cost

    # Calculate the difference in cost
    cost_difference = new_hay_cost - old_hay_cost

    # Display the difference in cost
    result = cost_difference
    return result

print(solution())