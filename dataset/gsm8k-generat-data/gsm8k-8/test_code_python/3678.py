def solution():
    # Define the initial height and growth rate
    initial_height = 5
    growth_rate = 3

    # Calculate the age at which the tree reaches the target height
    target_height = 23
    age = (target_height - initial_height) / growth_rate + 1

    # Round up to ensure the tree has reached the target height
    age = int(math.ceil(age))

    result = age
    return result

print(solution())