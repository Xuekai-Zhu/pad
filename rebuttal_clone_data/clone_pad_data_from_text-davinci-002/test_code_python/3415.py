def solution():
    kids_per_day = 8
    adults_per_day = 10
    price_per_kid = 3
    price_per_adult = 2 * price_per_kid
    total_revenue = kids_per_day * price_per_kid + adults_per_day * price_per_adult
    result = total_revenue
    return result

print(solution())