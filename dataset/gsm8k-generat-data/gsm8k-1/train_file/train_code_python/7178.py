def solution():
    """Three baskets A, B and C contain different numbers of differently colored marbles. Basket A contains 4 red marbles and 2 yellow marbles. Basket B contains 6 green marbles and 1 yellow marble. Basket C contains 3 white marbles and 9 yellow marbles. What is the difference between the number of each color of marble in the basket that has the greatest difference?"""
    basket_a = {"red": 4, "yellow": 2}
    basket_b = {"green": 6, "yellow": 1}
    basket_c = {"white": 3, "yellow": 9}
    
    basket_list = [basket_a, basket_b, basket_c]
    max_difference = 0
    
    for basket in basket_list:
        difference = 0
        for color, count in basket.items():
            if color == "yellow":
                continue
            else:
                if count > basket["yellow"]:
                    difference = count - basket["yellow"]
                else:
                    difference = basket["yellow"] - count
                if difference > max_difference:
                    max_difference = difference
                    
    result = max_difference
    return result

print(solution())