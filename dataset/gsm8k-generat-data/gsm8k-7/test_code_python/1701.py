def solution():
    total_weight = 120
    applesauce_weight = total_weight / 2
    pie_weight = total_weight - applesauce_weight
    apples_per_pie = 4
    num_pies = pie_weight / apples_per_pie
    result = num_pies
    return result

print(solution())