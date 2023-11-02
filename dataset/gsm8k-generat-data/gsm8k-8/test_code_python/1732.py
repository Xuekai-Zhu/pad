def solution():
    # Calculate the total number of scoops
    total_scoops = 10 * 3

    # Subtract the number of scoops Ethan wants
    total_scoops -= 2

    # Subtract the number of scoops Lucas, Danny and Connor want
    total_scoops -= 2 * 3

    # Subtract the number of scoops Olivia wants
    total_scoops -= 2

    # Subtract the number of scoops Shannon wants
    total_scoops -= 2 * 2

    result = total_scoops
    return result

print(solution())