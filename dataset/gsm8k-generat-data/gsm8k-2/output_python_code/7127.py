def solution():
    """Blake needs to prime and paint 5 rooms in his house. Each room will require a gallon of primer and a gallon of paint. Currently the primer is $30.00 a gallon and they are offering 20% off. The paint costs $25.00 a gallon and is not on sale. How much will he spend on paint and primer?"""
    rooms = 5
    primer_price = 30
    primer_discount = 0.2
    paint_price = 25
    total_primer_price = rooms * primer_price * (1 - primer_discount)
    total_paint_price = rooms * paint_price
    total_cost = total_primer_price + total_paint_price
    result = total_cost
    return result

print(solution())