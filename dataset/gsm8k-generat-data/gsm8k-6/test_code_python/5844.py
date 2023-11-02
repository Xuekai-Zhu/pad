def solution():
    # Let x be the smallest odd integer, then the next two odd integers are x+2 and x+4
    # Their sum is -147, so we can write an equation:
    # x + (x+2) + (x+4) = -147
    # Solving for x, we get x = -51
    # Therefore, the largest number is x+4 = -47
    largest_number = -47
    result = largest_number
    return result

print(solution())