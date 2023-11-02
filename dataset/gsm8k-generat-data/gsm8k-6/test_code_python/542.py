def solution():
    # Calculate the total number of cakes left after Carol eats 12
    total_cakes = 10 * 5 - 12  # Sara bakes 10 cakes every day for 5 days, Carol eats 12
    cans_of_frosting = total_cakes * 2  # It takes 2 cans of frosting to frost a single cake
    result = cans_of_frosting
    return result

print(solution())