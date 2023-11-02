def solution():
    """Damien collects glasses for a hobby and decides he wants to put them in display cupboards. His tall cupboard can hold 20 glasses, his wide cupboard can hold twice as many, and his narrow cupboard can hold 15 glasses with the glasses divided equally among the three shelves. As Damien is putting glasses in the narrow cupboard, he accidentally breaks one of the shelves. If all of the cupboards are full, how many glasses are currently being displayed?"""
    # Define the maximum number of glasses that each cupboard can hold
    TALL_CAPACITY = 20
    WIDE_CAPACITY = 2 * TALL_CAPACITY
    NARROW_CAPACITY = 15 * 3

    # Calculate the total number of glasses that can be displayed before the shelf is broken
    total_capacity = TALL_CAPACITY + WIDE_CAPACITY + NARROW_CAPACITY

    # Calculate the number of glasses currently being displayed
    glasses_displayed = total_capacity - 1 * 15

    # Display the number of glasses currently being displayed
    result = glasses_displayed
    return result

print(solution())