def solution():
    # Calculate the amount of tomatoes harvested on Thursday
    thursday_harvest = 400 / 2

    # Calculate the amount of tomatoes harvested on Friday
    friday_harvest = 2000 - 400 - thursday_harvest

    # Calculate the amount of tomatoes remaining on Friday after giving away 700kg
    remaining_tomatoes = friday_harvest - 700
    result = remaining_tomatoes
    return result

print(solution())