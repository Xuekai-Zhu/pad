def solution():
    # Let x be the number of poets
    # Then x + 50 is the number of tree huggers, which is 120
    x = 70  # Solving for x, we get x = 70

    # The total number of students is 400
    # So the number of singers is 400 - (x + (x + 50))
    # Simplifying, we get 400 - 2x - 50 = 350 - 2x
    # Therefore, the number of singers is 350 - 2x
    singers = 210  # Substituting x = 70, we get singers = 210

    result = singers
    return result

print(solution())