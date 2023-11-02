def solution():
    num_gyms = 20
    num_bikes_per_gym = 10
    num_treadmills_per_gym = 5
    num_ellipticals_per_gym = 5

    bike_price = 700
    treadmill_price = bike_price * 1.5
    elliptical_price = treadmill_price * 2

    # Calculate the total cost of all bikes
    total_bikes_cost = num_gyms * num_bikes_per_gym * bike_price

    # Calculate the total cost of all treadmills
    total_treadmills_cost = num_gyms * num_treadmills_per_gym * treadmill_price

    # Calculate the total cost of all ellipticals
    total_ellipticals_cost = num_gyms * num_ellipticals_per_gym * elliptical_price

    # Calculate the total cost of replacing everything
    total_cost = total_bikes_cost + total_treadmills_cost + total_ellipticals_cost
    result = total_cost
    return result

print(solution())