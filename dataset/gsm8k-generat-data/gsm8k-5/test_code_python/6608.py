def solution():
    num_gyms = 20  # There are 20 gyms
    num_bikes_per_gym = 10  # Each gym has 10 bikes
    num_treadmills_per_gym = 5  # Each gym has 5 treadmills
    num_ellipticals_per_gym = 5  # Each gym has 5 elliptical machines
    bike_cost = 700  # Each bike costs $700
    treadmill_cost = 1.5 * bike_cost  # Each treadmill costs 50% more than a bike
    elliptical_cost = 2 * treadmill_cost  # Each elliptical costs twice as much as a treadmill

    # Calculate the total cost to replace all the bikes
    total_bike_cost = num_gyms * num_bikes_per_gym * bike_cost

    # Calculate the total cost to replace all the treadmills
    total_treadmill_cost = num_gyms * num_treadmills_per_gym * treadmill_cost

    # Calculate the total cost to replace all the elliptical machines
    total_elliptical_cost = num_gyms * num_ellipticals_per_gym * elliptical_cost

    # Calculate the grand total to replace everything
    grand_total = total_bike_cost + total_treadmill_cost + total_elliptical_cost
    result = grand_total
    return result

print(solution())