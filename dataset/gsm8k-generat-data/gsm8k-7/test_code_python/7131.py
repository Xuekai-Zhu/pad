def solution():
    morning_hours = 2
    morning_rate = 10.0

    afternoon_hours = 2
    afternoon_rate = 12.5

    weekend_hours = 4
    weekend_rate = 10.0

    num_weekdays = 5
    num_weekends = 2

    # Calculate the total earnings from morning dog walking
    morning_earnings = morning_rate * morning_hours * num_weekdays

    # Calculate the total earnings from afternoon card shop work
    afternoon_earnings = afternoon_rate * afternoon_hours * num_weekdays

    # Calculate the total earnings from weekend babysitting
    weekend_earnings = (weekend_rate * weekend_hours * num_weekends) + (10 * 4)

    # Calculate the total earnings over 7 days
    total_earnings = morning_earnings + afternoon_earnings + weekend_earnings
    result = total_earnings
    return result

print(solution())