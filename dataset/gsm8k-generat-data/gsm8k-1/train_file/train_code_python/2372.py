def solution():
    """There are 60 passengers on a bus. Children make up 25% of the bus riders. How many adults are on the bus?"""
    total_passengers = 60
    children_percent = 25
    children_count = total_passengers * (children_percent / 100)
    adult_count = total_passengers - children_count
    result = adult_count
    return result

print(solution())