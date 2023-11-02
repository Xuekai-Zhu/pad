def solution():
    """Troy makes soup. He buys 4 pounds of beef and 6 pounds of vegetables. The vegetables cost $2 per pound and the beef is 3 times that price. How much does everything cost?"""
    beef_pounds = 4
    vegetable_pounds = 6
    vegetable_price = 2
    beef_price = 3 * vegetable_price
    total_cost = (beef_pounds * beef_price) + (vegetable_pounds * vegetable_price)
    result = total_cost
    return result

print(solution())