def solution():
    """Teresa sells large stuffed animals for three times the price of small stuffed animals. Today, she sold twice as many small stuffed animals as large ones and earned $120 from the sales. Each small stuffed animal costs $4. How many small stuffed animals did she sell?"""
    large_price = 3*4 #price of one large stuffed animal
    total_sales = 120 #total amount earned
    large_qty = total_sales/(2*large_price) #quantity of large stuffed animals sold
    small_qty = 2*large_qty #quantity of small stuffed animals sold
    result = small_qty
    return result

print(solution())