def solution():
    # Define the number of gyms and machines in each gym
    num_gyms = 20
    num_bikes = 10
    num_treadmills = 5
    num_ellipticals = 5

    # Define the cost of each machine
    bike_cost = 700
    treadmill_cost = 1.5 * bike_cost
    elliptical_cost = 2 * treadmill_cost

    # Calculate the total cost of each type of machine for all gyms
    total_bike_cost = num_gyms * num_bikes * bike_cost
    total_treadmill_cost = num_gyms * num_treadmills * treadmill_cost
    total_elliptical_cost = num_gyms * num_ellipticals * elliptical_cost

    # Calculate the total cost of replacing all machines
    total_cost = total_bike_cost + total_treadmill_cost + total_elliptical_cost
    result = total_cost
    return result

print(solution())