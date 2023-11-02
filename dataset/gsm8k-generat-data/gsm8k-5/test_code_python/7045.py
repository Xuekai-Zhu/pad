def solution():
    cleaning_time = 1.5  # Jackson spends three times as long cleaning the bathroom as washing dishes
    total_time = 2*2 + 0.5 + cleaning_time  # Jackson spends 2 hours vacuuming twice, plus 0.5 hours washing dishes, plus cleaning time for the bathroom
    spending_money = total_time * 5  # Jackson earns $5 per hour spent on chores

    result = spending_money
    return result

print(solution())