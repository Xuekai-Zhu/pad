def solution():
    price_per_kilo = 2  # Oliver charges $2 per kilo of laundry

    # Calculate the total weight of laundry washed in three days
    total_laundry_weight = 5 + (5 + 5) + (2 * (5 + 5))

    # Calculate the total earnings for three days
    total_earnings = price_per_kilo * total_laundry_weight
    result = total_earnings
    return result

print(solution())