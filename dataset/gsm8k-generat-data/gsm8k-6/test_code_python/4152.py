def solution():
    # Calculate the total cost of buying and replacing the coats over 30 years
    expensive_cost = 300 * 2  # the expensive coat lasts for 15 years, so it will need to be replaced twice in 30 years
    cheap_cost = 120 * 6  # the cheap coat lasts for 5 years, so it will need to be replaced 6 times in 30 years

    # Calculate the total cost savings of buying the more expensive coat
    savings = cheap_cost - expensive_cost
    result = savings
    return result

print(solution())