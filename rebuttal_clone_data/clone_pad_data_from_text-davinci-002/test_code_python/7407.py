def solution():
    students_buying_2 = 2
    students_buying_3 = 6
    students_buying_1 = 2
    pencils_bought_2 = 2 * students_buying_2
    pencils_bought_3 = 3 * students_buying_3
    pencils_bought_1 = 1 * students_buying_1
    total_pencils = pencils_bought_2 + pencils_bought_3 + pencils_bought_1
    result = total_pencils
    
    return result

print(solution())