def solution():
    # Set up equations to solve for the weight of Kevin's briefcase and laptop
    # k = weight of Kevin's briefcase when empty
    # 2k = weight of Karen's tote bag
    # 2(2k + w) = weight of Kevin's briefcase when laptop and papers are added
    # w = weight of laptop
    # (2k + w)/6 = weight of Kevin's work papers
    k = 4  # Solve for k based on given information
    w = (2 * k + k) / 2 - 2 * k  # Solve for weight of laptop based on given information
    weight_difference = w - 8  # Calculate the weight difference between the laptop and Karen's tote
    result = weight_difference
    return result

print(solution())