def solution():
    
    total_items = 7 + 4
    total_sales = 69
    shirt_price = 5
    total_shirt_sales = shirt_price * 4
    total_dress_sales = total_sales - total_shirt_sales
    dress_price = total_dress_sales / 7
    result = dress_price
    return result

print(solution())