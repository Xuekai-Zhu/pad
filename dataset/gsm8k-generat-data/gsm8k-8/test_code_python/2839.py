def solution():
    # Calculate how many s'mores Jacob can make with the current amount of ingredients
    num_smores = min(48 // 2, 6 // 1)

    # Calculate the remaining graham crackers and marshmallows
    remaining_graham = 48 - num_smores * 2
    remaining_marshmallow = 6 - num_smores * 1

    # Calculate how many more marshmallows Jacob needs to buy
    more_marshmallows = max(0, num_smores * 1 - remaining_marshmallow)

    result = more_marshmallows
    return result

print(solution())