def solution():
    # Calculate the total number of whales
    first_trip_male = 28
    first_trip_female = 2 * first_trip_male
    second_trip = 8 + 8 + 8  # 8 baby whales each travelling with their parents
    third_trip_male = first_trip_male / 2
    third_trip_female = first_trip_female

    total_whales = first_trip_male + first_trip_female + second_trip + third_trip_male + third_trip_female
    result = total_whales
    return result

print(solution())