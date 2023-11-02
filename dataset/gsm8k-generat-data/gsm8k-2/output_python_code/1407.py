def solution():
    """Nicki spent the last year running a lot. For the first half of the year, she ran a total of 20 miles per week. For the second half of the year, she increased the mileage to 30 miles per week. How many miles total did she run for the year?"""
    first_half = 20 * 26  # 26 weeks in first half of year
    second_half = 30 * 26  # 26 weeks in second half of year
    total_miles = first_half + second_half
    result = total_miles
    return result

print(solution())