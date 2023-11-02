def solution():
    """Blake needs to prime and paint 5 rooms in his house. Each room will require a gallon of primer and a gallon of paint. Currently the primer is $30.00 a gallon and they are offering 20% off. The paint costs $25.00 a gallon and is not on sale. How much will he spend on paint and primer?"""
    num_rooms = 5
    primer_price = 30 * 0.8
    paint_price = 25
    total_cost = (primer_price + paint_price) * num_rooms
    result = total_cost
    return result

print(solution())