def solution():
    """Abraham owns 80 square meters of unused land. He sold half of the land for $50, and after a month, he sold another 1/4 of his land for $30. He then sold the remaining land for $3 per square meter. How much money will he be able to earn after selling all his unused land?"""
    total_land = 80
    first_sale = total_land / 2
    second_sale = total_land * (1/4)
    third_sale = total_land - first_sale - second_sale
    
    total_money = (first_sale * 50) + (second_sale * 30) + (third_sale * 3)
    result = total_money
    return result

print(solution())