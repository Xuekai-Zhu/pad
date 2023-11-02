def solution():
    """Jeremy's uncle gave him $50 to spend on basketball equipment. He bought 5 jerseys that cost $2 each, a basketball that cost $18, and a pair of shorts that cost $8. How much money does Jeremy have left?"""
    money_given = 50
    num_jerseys = 5
    cost_per_jersey = 2
    basketball_cost = 18
    shorts_cost = 8
    
    total_cost = (num_jerseys * cost_per_jersey) + basketball_cost + shorts_cost
    money_left = money_given - total_cost
    result = money_left
    
    return result

print(solution())