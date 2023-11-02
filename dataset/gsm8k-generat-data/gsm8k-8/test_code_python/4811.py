def solution():
    # Calculate the number of people with brown eyes
    brown_eyes = 0.5 * 100

    # Calculate the number of people with black eyes
    black_eyes = 0.25 * 100

    # Calculate the number of people with blue eyes
    blue_eyes = 19

    # Calculate the number of people with green eyes
    green_eyes = 100 - (brown_eyes + black_eyes + blue_eyes)

    result = green_eyes
    return result

print(solution())