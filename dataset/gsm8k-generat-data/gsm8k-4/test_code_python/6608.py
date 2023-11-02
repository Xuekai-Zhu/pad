def solution():
    """A global gym decides to replace all of its cardio machines. They have 20 gyms. Each gym has 10 bikes, 5 treadmills, and 5 elliptical machines. The bikes cost $700 each. The treadmills cost 50% more than that. The elliptical machines are twice as expensive as the treadmills. How much does it cost to replace everything?"""
    # Define the prices of the different machines
    bike_price = 700
    treadmill_price = bike_price * 1.5
    elliptical_price = treadmill_price * 2

    # Calculate the total cost of machines for each gym
    gym_cost = (10 * bike_price) + (5 * treadmill_price) + (5 * elliptical_price)

    # Calculate the total cost of machines for all 20 gyms
    total_cost = gym_cost * 20

    result = total_cost
    return result

print(solution())