def solution():
    """Tedra is harvesting his tomatoes. He harvests 400 kg on Wednesday, and half as much on Thursday. He harvests a total of 2000 kg on Wednesday, Thursday, and Friday. How many tomatoes of the number he harvested on Friday are remaining if he gives away 700kg of them to his friends?"""
    # Calculate the amount harvested on Thursday
    thursday_harvest = 400 / 2

    # Calculate the total harvest for the three days
    total_harvest = 2000

    # Calculate the amount harvested on Friday
    friday_harvest = total_harvest - 400 - thursday_harvest

    # Calculate the remaining harvest after giving away 700kg
    remaining_harvest = friday_harvest - 700

    # Display the remaining harvest
    result = remaining_harvest
    return result

print(solution())