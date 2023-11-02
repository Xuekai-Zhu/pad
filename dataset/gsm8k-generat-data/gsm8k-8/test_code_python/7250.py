def solution():
    # Calculate the number of car wheels the guests bring
    guest_cars = 10
    guest_wheels = guest_cars * 4

    # Calculate the total number of car wheels in the parking lot
    total_wheels = guest_wheels + 8   # 8 for Dylan's parents' cars

    result = total_wheels
    return result

print(solution())