def solution():
    cakes_per_child = 4  # Ginger bakes 4 cakes per child each year
    cakes_per_husband = 7  # Ginger bakes 7 cakes for her husband each year
    cakes_for_parents = 2  # Ginger bakes 2 cakes each year for her parents

    total_cakes = (cakes_per_child * 2) + cakes_per_husband + (cakes_for_parents * 2) # 2 children plus husband, plus parents
    total_years = 10 # Ginger will be making cakes for 10 years

    # Calculate the total number of cakes Ginger will make in 10 years
    total_cakes_made = total_cakes * total_years
    result = total_cakes_made
    return result

print(solution())