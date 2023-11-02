def solution():
    """A global gym decides to replace all of its cardio machines. They have 20 gyms. Each gym has 10 bikes, 5 treadmills, and 5 elliptical machines. The bikes cost $700 each. The treadmills cost 50% more than that. The elliptical machines are twice as expensive as the treadmills. How much does it cost to replace everything?"""
    num_gyms = 20
    num_bikes = 10
    num_treadmills = 5
    num_ellipticals = 5
    bike_cost = 700
    treadmill_cost = bike_cost * 1.5
    elliptical_cost = treadmill_cost * 2
    total_cost = (num_bikes * bike_cost + num_treadmills * treadmill_cost + num_ellipticals * elliptical_cost) * num_gyms
    result = total_cost
    return result

print(solution())