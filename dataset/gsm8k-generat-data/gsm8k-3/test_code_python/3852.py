def solution():
    """John has to replace the ball bearings for machines he works with.  He has 10 machines and they take 30 ball bearings each.  It normally costs $1 per ball bearing but right now there is a sale where they are only $.75.  Also since he is buying in bulk he gets a further 20% discount.  How much money did he save by buying them all during the sale rather than 1 at a time?"""
    # Define the regular cost per ball bearing and the discounted cost during the sale
    REGULAR_COST = 1
    DISCOUNTED_COST = 0.75

    # Define the number of machines and ball bearings needed for each machine
    num_machines = 10
    num_bearings_per_machine = 30

    # Calculate the total number of ball bearings needed
    total_bearings = num_machines * num_bearings_per_machine

    # Calculate the regular cost and discounted cost for all the ball bearings
    regular_cost = total_bearings * REGULAR_COST
    discounted_cost = total_bearings * DISCOUNTED_COST * 0.8  # 20% discount

    # Calculate the amount of money saved by buying during the sale
    savings = regular_cost - discounted_cost

    # Display the amount of money saved
    result = savings
    return result

print(solution())