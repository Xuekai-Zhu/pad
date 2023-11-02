def solution():
    """Mark is filling a punch bowl that can hold 16 gallons of punch. He fills it part way, then his cousin comes along and drinks half the punch in the bowl. Mark starts to refill the bowl and adds 4 more gallons, but then his friend Sally comes in and drinks 2 more gallons of punch. After that, Mark has to add 12 gallons of punch to completely fill the bowl. How much punch did Mark initially add to the bowl?"""
    total_punch = 16
    half_punch = total_punch / 2
    initial_punch = half_punch + 4
    remaining_punch = initial_punch - 2
    final_punch = total_punch
    initial_addition = initial_punch - remaining_punch - final_punch
    result = initial_addition
    return result

print(solution())