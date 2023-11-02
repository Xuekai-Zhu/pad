def solution():
    """ Damien collects glasses for a hobby and decides he wants to put them in display cupboards. His tall cupboard can hold 20 glasses, his wide cupboard can hold twice as many, and his narrow cupboard can hold 15 glasses with the glasses divided equally among the three shelves. As Damien is putting glasses in the narrow cupboard, he accidentally breaks one of the shelves. If all of the cupboards are full, how many glasses are currently being displayed?"""
    tall_cupboard_capacity = 20
    wide_cupboard_capacity = 2 * tall_cupboard_capacity
    narrow_cupboard_capacity = 3 * 15 # 3 shelves, each holding 15 glasses
    glasses_displayed = tall_cupboard_capacity + wide_cupboard_capacity + narrow_cupboard_capacity - 1 # subtracting one for the broken shelf
    result = glasses_displayed
    return result

print(solution())