def solution():
    """Troy makes soup. He buys 4 pounds of beef and 6 pounds of vegetables. The vegetables cost $2 per pound and the beef is 3 times that price. How much does everything cost?"""
    beef_cost = 2 * 3  # $6 per pound
    vegetables_cost = 2  # $2 per pound
    total_cost = (4 * beef_cost) + (6 * vegetables_cost)
    result = total_cost
    return result

print(solution())