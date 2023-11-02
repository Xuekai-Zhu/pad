def solution():
    """Jeremy is driving 600 miles to visit his parents. His average speed for this trip is 50 miles per hour. Every two hours of driving, he makes a rest stop for 15 minutes. His car gets 18 miles per gallon of gas, and his gas indicator comes on when he's used 15 gallons, at which point he stops to refill, which takes 10 minutes. How long, in minutes, does he take to get to his parents' house, if he starts out with a full tank of gas?"""
    distance = 600
    speed = 50
    rest_time = 15
    refuel_time = 10
    mpg = 18
    gas_capacity = 15
    gas_used = (distance/mpg)
    stops = gas_used//gas_capacity
    total_time = (distance/speed)*60 + stops*rest_time + stops*refuel_time
    result = total_time
    return result

print(solution())