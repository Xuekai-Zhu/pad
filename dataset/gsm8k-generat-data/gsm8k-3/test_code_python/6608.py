def solution():
    """A global gym decides to replace all of its cardio machines.  They have 20 gyms.  Each gym has 10 bikes, 5 treadmills, and 5 elliptical machines.  The bikes cost $700 each.  The treadmills cost 50% more than that.  The elliptical machines are twice as expensive as the treadmills.  How much does it cost to replace everything?"""
    # Define the costs of each type of machine
    BIKE_COST = 700
    TREADMILL_COST = BIKE_COST * 1.5
    ELLIPTICAL_COST = TREADMILL_COST * 2

    # Define the number of each type of machine at each gym
    num_bikes = 10
    num_treadmills = 5
    num_ellipticals = 5

    # Calculate the cost of each type of machine at each gym
    gym_cost = (num_bikes * BIKE_COST) + (num_treadmills * TREADMILL_COST) + (num_ellipticals * ELLIPTICAL_COST)

    # Calculate the total cost of replacing all machines at all gyms
    total_cost = gym_cost * 20

    # Display the total cost
    result = total_cost
    return result

print(solution())