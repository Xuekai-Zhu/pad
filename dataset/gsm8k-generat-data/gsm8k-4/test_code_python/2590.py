def solution():
    """Damien collects glasses for a hobby and decides he wants to put them in display cupboards. His tall cupboard can hold 20 glasses, his wide cupboard can hold twice as many, and his narrow cupboard can hold 15 glasses with the glasses divided equally among the three shelves. As Damien is putting glasses in the narrow cupboard, he accidentally breaks one of the shelves. If all of the cupboards are full, how many glasses are currently being displayed?"""
    # Define the maximum capacities of the cupboards
    tall_capacity = 20
    wide_capacity = tall_capacity * 2
    narrow_capacity = 15 * 2  # double because one shelf is broken

    # Calculate the number of glasses in the narrow cupboard before the shelf was broken
    narrow_before = narrow_capacity / 3 * 2

    # Calculate the total number of glasses
    total_glasses = tall_capacity + wide_capacity + narrow_before

    # return the result
    result = total_glasses
    return result

print(solution())