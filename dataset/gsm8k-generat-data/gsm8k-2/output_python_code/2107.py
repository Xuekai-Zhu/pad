def solution():
    """Adam bought 15 apples on Monday. On Tuesday he bought 3 times that quantity. On Wednesday he bought 4 times the quantity he bought on Tuesday. What is the total quantity Adam bought on these three days?"""
    monday_quantity = 15
    tuesday_quantity = 3 * monday_quantity
    wednesday_quantity = 4 * tuesday_quantity
    total_quantity = monday_quantity + tuesday_quantity + wednesday_quantity
    result = total_quantity
    return result

print(solution())