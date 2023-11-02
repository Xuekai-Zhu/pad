def solution():
    difference_in_price = (120 - 90)
    price_of_banana = difference_in_price
    price_of_pear = 90
    total_price_of_oranges = 200 * price_of_banana
    total_price_of_pears = price_of_pear * 2
    total_price = total_price_of_oranges + total_price_of_pears
    result = total_price
    return result

print(solution())