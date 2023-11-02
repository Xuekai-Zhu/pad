def solution():
    """Tedra is harvesting his tomatoes. He harvests 400 kg on Wednesday, and half as much on Thursday. He harvests a total of 2000 kg on Wednesday, Thursday, and Friday. How many tomatoes of the number he harvested on Friday are remaining if he gives away 700kg of them to his friends?"""
    # Calculate the number of tomatoes harvested on Thursday
    thursday_harvest = 400 / 2

    # Calculate the number of tomatoes harvested on Friday
    friday_harvest = 2000 - 400 - thursday_harvest

    # Calculate the number of tomatoes remaining after giving some to friends
    remaining_tomatoes = friday_harvest - 700

    # return the result
    result = remaining_tomatoes
    return result

print(solution())