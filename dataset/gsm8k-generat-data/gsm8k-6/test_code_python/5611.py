def solution():
    # Calculate the total number of people who went on the hike
    car_passengers = 3 * 4  # 4 people in each car
    taxi_passengers = 6 * 6  # 6 people in each taxi
    van_passengers = 2 * 5  # 5 people in each van
    total_passengers = car_passengers + taxi_passengers + van_passengers

    result = total_passengers
    return result

print(solution())