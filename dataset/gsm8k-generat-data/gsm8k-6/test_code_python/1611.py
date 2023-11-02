def solution():
    # Calculate the total miles traveled in 3 days
    day_2 = (3/4) * 200  # On the second day, they traveled 3/4 as far as the first day
    first_2_days = 200 + day_2  # first two days combined
    day_3 = (1/2) * first_2_days  # they traveled 1/2 as many miles on the third day as the first two days combined
    total_miles = 200 + day_2 + day_3
    result = total_miles
    return result

print(solution())