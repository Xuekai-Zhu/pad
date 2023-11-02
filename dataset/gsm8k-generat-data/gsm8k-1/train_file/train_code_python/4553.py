def solution():
    """Michael ran a bakeshop and had to fill an order for 5 peach pies, 4 apple pies and 3 blueberry pies. Each pie recipe called for 3 pounds of fruit each. At the market, produce was on sale for $1.00 per pound for both blueberries and apples. The peaches each cost $2.00 per pound. How much will Michael spend at the market buying the fruit for his pie order?"""
    peach_pies = 5
    apple_pies = 4
    blueberry_pies = 3
    pounds_of_fruit_per_pie = 3
    peach_price_per_pound = 2
    apple_price_per_pound = 1
    blueberry_price_per_pound = 1
    total_cost = (peach_pies * pounds_of_fruit_per_pie * peach_price_per_pound) + (apple_pies * pounds_of_fruit_per_pie * apple_price_per_pound) + (blueberry_pies * pounds_of_fruit_per_pie * blueberry_price_per_pound)
    result = total_cost
    return result

print(solution())