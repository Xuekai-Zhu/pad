def solution():
    # Use the formula: carpenters * chairs * time = constant
    # we are given: 8 carpenters * 50 chairs * 10 days = constant
    constant = 8 * 50 * 10

    # To find the number of carpenters needed to make 75 chairs in 10 days, we rearrange the formula to get:
    carpenters_needed = constant / (75 * 10)
    result = carpenters_needed
    return result

print(solution())