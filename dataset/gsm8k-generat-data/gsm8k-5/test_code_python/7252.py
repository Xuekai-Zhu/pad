def solution():
    price_per_gallon_NC = 2.00
    price_per_gallon_VA = price_per_gallon_NC + 1.00  # Jim pays $1.00 more per gallon in Virginia
    gallons_NC = 10
    gallons_VA = 10
    total_cost = (price_per_gallon_NC * gallons_NC) + (price_per_gallon_VA * gallons_VA)
    result = total_cost
    return result

print(solution())