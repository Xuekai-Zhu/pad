def solution():
    male_whales_first_trip = 28
    female_whales_first_trip = 2 * male_whales_first_trip
    baby_whales = 8
    parent_whales = baby_whales / 2
    total_whales_first_trip = male_whales_first_trip + female_whales_first_trip + parent_whales
    male_whales_third_trip = male_whales_first_trip / 2
    female_whales_third_trip = female_whales_first_trip
    total_whales_third_trip = male_whales_third_trip + female_whales_third_trip
    total_whales = total_whales_first_trip + total_whales_second_trip + total_whales_third_trip
    result = total_whales
    return result

print(solution())