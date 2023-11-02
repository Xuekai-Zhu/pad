def solution():
    """Tommy is making steaks for his family. There are 5 of them in total. If each member wants one pound and the steaks are 20 ounces each, how many does he need to buy?"""
    # Define the number of people and the desired weight per person
    num_people = 5
    desired_weight = 16

    # Convert the steak weight from ounces to pounds
    steak_weight = 20 / 16

    # Calculate the total weight of steak needed
    total_weight = num_people * desired_weight

    # Calculate the number of steaks needed
    num_steaks = total_weight / steak_weight

    # Round up to the nearest whole number
    num_steaks = math.ceil(num_steaks)

    result = num_steaks
    return result

print(solution())