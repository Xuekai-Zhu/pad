def solution():
    
    samoa_boxes = 3
    samoa_price = 4
    thinmint_boxes = 2
    thinmint_price = 3.5
    fudge_boxes = 1
    fudge_price = 5
    sugar_boxes = 9
    sugar_price = 2

    samoa_sales = samoa_boxes * samoa_price
    thinmint_sales = thinmint_boxes * thinmint_price
    fudge_sales = fudge_boxes * fudge_price
    sugar_sales = sugar_boxes * sugar_price

    total_sales = samoa_sales + thinmint_sales + fudge_sales + sugar_sales
    result = total_sales
    return result

print(solution())