def solution():
    """Jeremy is driving 600 miles to visit his parents. His average speed for this trip is 50 miles per hour. Every two hours of driving, he makes a rest stop for 15 minutes. His car gets 18 miles per gallon of gas, and his gas indicator comes on when he's used 15 gallons, at which point he stops to refill, which takes 10 minutes. How long, in minutes, does he take to get to his parents' house, if he starts out with a full tank of gas?"""
    total_distance = 600
    average_speed = 50
    rest_time = (total_distance // (average_speed * 2)) * 15
    refuel_time = 10
    total_driving_time = total_distance / average_speed
    gas_consumption = total_distance / 18
    num_refuels = gas_consumption // 15
    total_refuel_time = num_refuels * refuel_time
    total_travel_time = total_driving_time + rest_time + total_refuel_time
    result = total_travel_time * 60
    return result

print(solution())