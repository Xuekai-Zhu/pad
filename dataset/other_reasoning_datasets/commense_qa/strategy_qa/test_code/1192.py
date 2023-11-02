def solution():
    newsstand_price = 5.99
    cost_per_eclipse = 1/6 # Since there were 6 eclipses in 2009
    total_cost_of_eclipses = cost_per_eclipse * 6 # Total cost of all eclipses in 2009
    if total_cost_of_eclipses >= newsstand_price:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())