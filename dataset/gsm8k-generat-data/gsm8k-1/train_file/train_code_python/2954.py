def solution():
    """Mo is buying valentine's day cards for the class. There are 30 students and he wants to give a Valentine to 60% of them. They cost $2 each. If he has $40, what percentage of his money will he spend on Valentine?"""
    num_students = 30
    percent_to_gift = 0.6
    num_valentines = round(num_students * percent_to_gift)
    cost_per_valentine = 2
    total_cost = num_valentines * cost_per_valentine
    budget = 40
    percent_spent = (total_cost / budget) * 100
    result = percent_spent
    return result

print(solution())