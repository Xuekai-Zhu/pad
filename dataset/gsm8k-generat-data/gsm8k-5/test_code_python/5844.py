def solution():
    # Let x be the smallest odd integer
    # Then the next two consecutive odd integers are x+2 and x+4
    # The sum of the three consecutive odd integers is x + (x+2) + (x+4) = 3x + 6
    # Given that the sum is -147, we have: 3x + 6 = -147
    # Solving for x: x = (-147 - 6) / 3 = -51

    # Therefore, the smallest odd integer is -51
    # The largest odd integer is x+4 = -51 + 4 = -47
    result = -47
    return result

print(solution())