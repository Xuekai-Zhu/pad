def solution():
    initial_price = 104  # price of the monster box of cereal before the reduction
    reduced_price = initial_price - 24  # price of the monster box of cereal after the reduction
    number_of_boxes = 20  # number of monster boxes of cereal Romina bought
    total_price = reduced_price * number_of_boxes  # total price Romina paid for the boxes
    result = total_price
    return result

print(solution())