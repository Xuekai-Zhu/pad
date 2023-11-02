def solution():
    """Toula went to the bakery and bought various types of pastries. She bought 3 dozen donuts which cost $68 per dozen, 2 dozen mini cupcakes which cost $80 per dozen, and 6 dozen mini cheesecakes for $55 per dozen. How much was the total cost?"""
    donut_cost = 68 * 3
    cupcake_cost = 80 * 2
    cheesecake_cost = 55 * 6
    total_cost = donut_cost + cupcake_cost + cheesecake_cost
    result = total_cost
    return result

print(solution())