def solution():
    """Mark is filling a punch bowl that can hold 16 gallons of punch. He fills it part way, then his cousin comes along and drinks half the punch in the bowl. Mark starts to refill the bowl and adds 4 more gallons, but then his friend Sally comes in and drinks 2 more gallons of punch. After that, Mark has to add 12 gallons of punch to completely fill the bowl. How much punch did Mark initially add to the bowl?"""
    # Define the total capacity of the punch bowl
    total_capacity = 16

    # Calculate the amount of punch remaining after Mark's cousin drinks half
    remaining_after_cousin = total_capacity / 2

    # Calculate the amount of punch remaining after Mark adds 4 more gallons
    remaining_after_mark = remaining_after_cousin + 4

    # Calculate the amount of punch remaining after Sally drinks 2 more gallons
    remaining_after_sally = remaining_after_mark - 2

    # Calculate the amount of punch initially added by Mark
    initial_punch = total_capacity - remaining_after_sally - 12

    # return the result
    result = initial_punch
    return result

print(solution())