def solution():
    """A swarm of ants discovered a pile of sugar that spilled from a dropped bag. They begin to harvest it and carry it off to their anthill. Every hour, the ants remove 4 ounces of sugar. The bag of sugar held 24 ounces before it was dropped. After three hours, how many more hours will the ants need to harvest the remaining sugar?"""
    # Define the amount of sugar in the bag before it was dropped
    initial_sugar = 24

    # Calculate the amount of sugar harvested in the first three hours
    three_hour_sugar = 4 * 3

    # Calculate the remaining sugar in the pile
    remaining_sugar = initial_sugar - three_hour_sugar

    # Calculate the remaining time needed to harvest all the sugar
    remaining_time = remaining_sugar / 4

    # Display the remaining time
    result = remaining_time
    return result

print(solution())