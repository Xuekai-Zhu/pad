def solution():
    cost_to_fix_sink = 30
    cost_to_fix_shower = 40
    cost_to_fix_toilet = 50
    first_job = cost_to_fix_sink * 3 + cost_to_fix_toilet * 3
    second_job = cost_to_fix_sink * 5 + cost_to_fix_toilet * 2
    third_job = cost_to_fix_sink * 3 + cost_to_fix_shower * 2 + cost_to_fix_toilet
    most_money = max(first_job, second_job, third_job)
    result = most_money
    return result

print(solution())