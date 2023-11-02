def solution():
    
    hotdog_weight = 2
    burger_weight = 5
    pie_weight = 10
    noah_burgers = 8
    jacob_pies = noah_burgers - 3
    mason_hotdogs = jacob_pies * 3
    mason_weight = mason_hotdogs * hotdog_weight
    result = mason_weight
    return result

print(solution())