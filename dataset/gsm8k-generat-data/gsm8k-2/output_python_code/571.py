def solution():
    """Steve wanted to make a total of $100 within four days, so he took on a berry-picking job in Sweden. The job paid $2 for every pound of lingonberries picked. On Monday he picked 8 pounds. Tuesday’s harvest was triple what he had picked the previous day. On Wednesday he felt very tired and decided to rest. How many pounds of lingonberries did Steve have to pick on Thursday?"""
    target_income = 100
    daily_income = 0
    monday_harvest = 8
    tuesday_harvest = monday_harvest * 3
    wednesday_harvest = 0
    total_harvest = monday_harvest + tuesday_harvest + wednesday_harvest
    total_income = total_harvest * 2
    remaining_income = target_income - total_income
    pounds_needed_on_thursday = remaining_income / 2
    result = pounds_needed_on_thursday
    return result

print(solution())