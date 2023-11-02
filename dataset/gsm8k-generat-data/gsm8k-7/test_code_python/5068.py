def solution():
    # Let x be the number of slices in the original loaf
    # Andy ate 3 slices, so there are x - 3 slices remaining
    # Emma makes 10 pieces of toast, which requires 2 slices each, so she used 20 slices total
    # There was 1 slice left, so we have the equation:
    # x - 3 - 20 = 1
    # Solving for x, we get:
    x = 24
    result = x
    return result

print(solution())