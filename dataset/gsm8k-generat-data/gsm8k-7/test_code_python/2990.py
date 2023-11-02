def solution():
    # Let x be the original number of jewels the dragon had
    # The dragon lost 3 jewels, so it had x-3 jewels
    # It gained twice as many jewels from the king's crown, so it has 2*(3) = 6 more jewels
    # The total number of jewels now is (x-3) + 6 = x + 3
    # The new jewels are a third of the original, so (x+3) = (1/3)*x
    # Solving for x:
    x = 9
    result = x
    return result

print(solution())