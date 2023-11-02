def solution():
    # Calculate the total amount of Vitamin A needed for the week
    weekly_VitaminA = 200 * 7  # recommended daily serving of Vitamin A is 200 mg, so weekly serving is 200*7 mg
    # Calculate the number of pills Ryan needs to take to get the recommended amount of Vitamin A for the week
    pills_needed = weekly_VitaminA / 50  # each pill has 50 mg of Vitamin A
    result = pills_needed
    return result

print(solution())