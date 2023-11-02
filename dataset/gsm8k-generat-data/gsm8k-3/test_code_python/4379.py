def solution():
    """Jeremy is driving 600 miles to visit his parents. His average speed for this trip is 50 miles per hour.
    Every two hours of driving, he makes a rest stop for 15 minutes. His car gets 18 miles per gallon of gas,
    and his gas indicator comes on when he's used 15 gallons, at which point he stops to refill,
    which takes 10 minutes. How long, in minutes, does he take to get to his parents' house, if he starts out with a full tank of gas?"""
    # Define the variables
    distance = 600
    speed = 50
    rest_time = 15
    refill_time = 10
    gas_capacity = 18
    gas_indicator = 15
    mpg = 18

    # Calculate the number of rest stops he makes
    rest_stops = distance // (2 * speed)

    # Calculate the total time he spends resting
    total_rest_time = rest_stops * rest_time

    # Calculate the number of times he needs to refill his gas tank
    gas_refills = distance // (gas_capacity * mpg)

    # Calculate the total time he spends refilling his gas tank
    total_refill_time = gas_refills * refill_time

    # Calculate the total time for the entire trip
    total_time = (distance / speed) * 60 + total_rest_time + total_refill_time

    return total_time

print(solution())