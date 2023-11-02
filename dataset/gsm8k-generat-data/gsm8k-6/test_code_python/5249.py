def solution():
    # Calculate the total number of cakes Ginger makes
    cakes_per_kid = 4 * 2  # Ginger bakes a cake for each child on 4 holidays
    cakes_for_husband = 7  # Ginger bakes a cake for her husband on 7 special occasions
    cakes_for_parents = 2  # Ginger bakes a cake for each parent on 1 holiday
    total_cakes = cakes_per_kid + cakes_for_husband + cakes_for_parents
    cakes_in_10_years = total_cakes * 10  # multiply by the number of years
    result = cakes_in_10_years
    return result

print(solution())