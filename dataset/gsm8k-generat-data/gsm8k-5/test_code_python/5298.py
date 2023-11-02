def solution():
    initial_stock = 2000  # Carla initially had 2000 cans of food
    people_day1 = 500  # 500 people showed up on the first day
    people_day2 = 1000  # 1000 people showed up on the second day
    cans_day1 = 500  # Each person took 1 can of food on the first day
    cans_day2 = 2000  # Each person took 2 cans of food on the second day

    # Calculate the total cans given away on the first day
    cans_given_day1 = people_day1 * cans_day1

    # Calculate the total cans given away on the second day
    cans_given_day2 = people_day2 * cans_day2

    # Calculate the total cans restocked
    total_restocked = 1500 + 3000

    # Calculate the total cans given away
    total_given_away = cans_given_day1 + cans_given_day2 + total_restocked - initial_stock
    result = total_given_away
    return result

print(solution())