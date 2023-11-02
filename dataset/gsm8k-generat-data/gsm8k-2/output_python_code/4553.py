def solution():
    """Michael ran a bakeshop and had to fill an order for 5 peach pies, 4 apple pies and 3 blueberry pies. Each pie recipe called for 3 pounds of fruit each. At the market, produce was on sale for $1.00 per pound for both blueberries and apples. The peaches each cost $2.00 per pound. How much will Michael spend at the market buying the fruit for his pie order?"""
    peach_price = 2
    apple_price = 1
    blueberry_price = 1
    pies = [5, 4, 3]
    fruit_per_pie = 3
    peach_total = pies[0] * fruit_per_pie * peach_price
    apple_total = pies[1] * fruit_per_pie * apple_price
    blueberry_total = pies[2] * fruit_per_pie * blueberry_price
    total_cost = peach_total + apple_total + blueberry_total
    result = total_cost
    return result

print(solution())