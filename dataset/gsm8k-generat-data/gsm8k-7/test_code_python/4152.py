def solution():
    expensive_coat_cost = 300
    expensive_coat_lifetime = 15
    cheap_coat_cost = 120
    cheap_coat_lifetime = 5
    num_years = 30

    # Calculate the total cost of buying the expensive coat
    total_expensive_cost = (expensive_coat_cost * num_years) / expensive_coat_lifetime

    # Calculate the total cost of buying the cheap coat
    total_cheap_cost = (cheap_coat_cost * num_years) / cheap_coat_lifetime

    # Calculate the cost savings of buying the expensive coat
    cost_savings = total_cheap_cost - total_expensive_cost
    result = cost_savings
    return result

print(solution())