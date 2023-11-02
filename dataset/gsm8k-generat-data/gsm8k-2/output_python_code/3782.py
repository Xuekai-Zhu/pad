def solution():
    """Bryce is bringing in doughnuts for his class. There are 25 students in his class, 10 kids want chocolate doughnuts and 15 want glazed doughnuts. The chocolate doughnuts cost $2 each and the glazed doughnuts cost $1 each. How much is the total cost for doughnuts?"""
    num_chocolate = 10
    num_glazed = 15
    cost_chocolate = 2
    cost_glazed = 1
    total_cost = num_chocolate * cost_chocolate + num_glazed * cost_glazed
    result = total_cost
    return result

print(solution())