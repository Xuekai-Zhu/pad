def solution():
    sum_of_integers = -147

    # Let x be the smallest odd integer, then the next two consecutive odd integers are x+2 and x+4
    # The sum of these three integers is x + (x+2) + (x+4) = 3x + 6 = 147
    # Solving for x, we get x = (147 - 6) / 3 = 47

    x = (sum_of_integers + 6) / 3
    largest_integer = x + 4
    result = largest_integer
    return result

print(solution())