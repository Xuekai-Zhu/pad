def solution():
    # Calculate the total number of days in two weeks
    total_days = 14

    # Calculate the number of shirts worn on weekdays
    weekday_shirts = 5

    # Calculate the number of shirts worn for after-school club
    club_shirts = 3 * 3

    # Calculate the number of shirts worn on Saturday and Sunday
    weekend_shirts = 2

    # Calculate the total number of shirts needed
    total_shirts = (weekday_shirts + club_shirts + weekend_shirts) * 2

    result = total_shirts
    return result

print(solution())