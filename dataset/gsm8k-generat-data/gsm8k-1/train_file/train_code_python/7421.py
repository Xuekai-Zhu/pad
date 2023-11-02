def solution():
    """Mark is filling a punch bowl that can hold 16 gallons of punch. He fills it part way, then his cousin comes along and drinks half the punch in the bowl. Mark starts to refill the bowl and adds 4 more gallons, but then his friend Sally comes in and drinks 2 more gallons of punch. After that, Mark has to add 12 gallons of punch to completely fill the bowl. How much punch did Mark initially add to the bowl?"""
    max_capacity = 16
    initial_amount = (max_capacity/2) + 4 + 2 + 12
    result = initial_amount
    return result

print(solution())