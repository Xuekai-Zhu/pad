def solution():
    """Vanessa has decided to sell some of her clothes to make pocket money, offering a standard price for each type of item. She made a total of $69 by selling 7 dresses and 4 shirts. If she managed to sell each shirt for $5, how much did the dresses sell for each?"""
    total_items = 7 + 4
    total_sales = 69
    shirt_price = 5
    total_shirt_sales = shirt_price * 4
    total_dress_sales = total_sales - total_shirt_sales
    dress_price = total_dress_sales / 7
    result = dress_price
    return result

print(solution())