def solution():
    olga_stripes = 3
    rick_stripes = olga_stripes - 1
    hortense_stripes = olga_stripes * 2

    # Calculate the total number of stripes between all three people
    total_stripes = (3 * olga_stripes) + (2 * rick_stripes) + (2 * hortense_stripes)
    result = total_stripes
    return result

print(solution())