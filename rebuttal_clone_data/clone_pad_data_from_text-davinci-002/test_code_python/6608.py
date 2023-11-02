def solution():
    num_gyms = 20
    num_bikes = 10
    num_treadmills = 5
    num_ellipticals = 5
    cost_bike = 700
    cost_treadmill = cost_bike * 1.5
    cost_elliptical = cost_treadmill * 2
    total_cost = (num_bikes * cost_bike) + (num_treadmills * cost_treadmill) + (num_ellipticals * cost_elliptical)
    result = total_cost
    return result

print(solution())