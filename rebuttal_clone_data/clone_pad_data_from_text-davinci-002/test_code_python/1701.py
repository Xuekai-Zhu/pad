def solution(pounds_of_apples):
    applesauce_weight = pounds_of_apples / 2
    pie_weight = pounds_of_apples - applesauce_weight
    apples_per_pie = 4
    pies = pie_weight / apples_per_pie
    result = pies
    
    return result

print(solution())