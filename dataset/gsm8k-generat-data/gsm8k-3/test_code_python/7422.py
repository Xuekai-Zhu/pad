def solution():
    """Mark is filling a punch bowl that can hold 16 gallons of punch. He fills it part way, then his cousin comes along and drinks half the punch in the bowl. Mark starts to refill the bowl and adds 4 more gallons, but then his friend Sally comes in and drinks 2 more gallons of punch. After that, Mark has to add 12 gallons of punch to completely fill the bowl. How much punch did Mark initially add to the bowl?"""
    # Define the capacity of the punch bowl
    capacity = 16

    # Calculate the amount of punch that Mark initially added to the bowl
    initial_amount = ((capacity/2) - 4 - 2 - 12)/2

    # Display the initial amount of punch added by Mark
    result = initial_amount
    return result

print(solution())