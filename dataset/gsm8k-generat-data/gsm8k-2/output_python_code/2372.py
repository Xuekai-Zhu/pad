def solution():
    """There are 60 passengers on a bus. Children make up 25% of the bus riders. How many adults are on the bus?"""
    total_passengers = 60
    children = total_passengers * 0.25
    adults = total_passengers - children
    result = adults
    return result

print(solution())