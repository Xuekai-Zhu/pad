def solution():
    
    num_gyms = 20
    num_bikes_per_gym = 10
    num_treadmills_per_gym = 5
    num_ellipticals_per_gym = 5

    bike_cost = 700
    treadmill_cost = 1.5 * bike_cost
    elliptical_cost = 2 * treadmill_cost

    total_cost = (num_gyms * (num_bikes_per_gym * bike_cost +
                              num_treadmills_per_gym * treadmill_cost +
                              num_ellipticals_per_gym * elliptical_cost))
    result = total_cost
    return result

print(solution())