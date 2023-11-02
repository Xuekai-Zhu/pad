def solution():
    canvas_co2 = 600
    plastic_co2_per_bag = 0.25   # 4 ounces = 0.25 pounds
    bags_per_trip = 8
    trips = 0

    while (canvas_co2 > (plastic_co2_per_bag * bags_per_trip)):
        trips += 1
        canvas_co2 -= (plastic_co2_per_bag * bags_per_trip)

    result = trips
    return result

print(solution())