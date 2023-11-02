def solution():
    """Three baskets A, B and C contain different numbers of differently colored marbles. Basket A contains 4 red marbles and 2 yellow marbles. Basket B contains 6 green marbles and 1 yellow marble. Basket C contains 3 white marbles and 9 yellow marbles. What is the difference between the number of each color of marble in the basket that has the greatest difference?"""
    basket_a = {'red': 4, 'yellow': 2}
    basket_b = {'green': 6, 'yellow': 1}
    basket_c = {'white': 3, 'yellow': 9}

    max_diff = 0
    for color in set(basket_a.keys()) | set(basket_b.keys()) | set(basket_c.keys()):
        counts = [basket_a.get(color, 0), basket_b.get(color, 0), basket_c.get(color, 0)]
        diff = max(counts) - min(counts)
        if diff > max_diff:
            max_diff = diff

    result = max_diff
    return result

print(solution())