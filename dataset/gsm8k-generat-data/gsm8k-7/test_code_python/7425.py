def solution():
    breads_per_hour = 10
    baguettes_per_two_hours = 30
    hours_per_day = 6

    # Calculate the total breads made in 6 hours
    breads_made = (breads_per_hour * hours_per_day) + (baguettes_per_two_hours * (hours_per_day // 2))

    result = breads_made
    return result

print(solution())