def solution():
    """A bus has a carrying capacity of 80 people. At the first pickup point, the number of people who entered the bus was 3/5 of its carrying capacity. If there were 50 people at the next pick-up point, how many people could not take the bus because it was full?"""
    carrying_capacity = 80
    first_pickup = carrying_capacity * 3/5
    total_passengers = first_pickup + 50
    excess_passengers = total_passengers - carrying_capacity
    
    if excess_passengers < 0:
        result = 0
    else:
        result = excess_passengers
        
    return result

print(solution())