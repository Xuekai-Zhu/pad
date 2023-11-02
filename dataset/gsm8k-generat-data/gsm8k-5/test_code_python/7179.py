def solution():
    # Count the number of each color of marble in each basket
    basket_a = {"red": 4, "yellow": 2}
    basket_b = {"green": 6, "yellow": 1}
    basket_c = {"white": 3, "yellow": 9}

    # Find the maximum difference in the number of marbles of any color between any two baskets
    max_difference = 0
    for color in basket_a:
        difference = abs(basket_a[color] - basket_b.get(color, 0))
        difference = max(difference, abs(basket_a[color] - basket_c.get(color, 0)))
        difference = max(difference, abs(basket_b.get(color, 0) - basket_c.get(color, 0)))
        if difference > max_difference:
            max_difference = difference

    result = max_difference
    return result

print(solution())