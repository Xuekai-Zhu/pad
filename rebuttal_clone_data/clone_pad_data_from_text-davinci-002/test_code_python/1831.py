def solution():
    number_of_pens = 2 * 300
    number_of_pencils = 15 * 80
    total_number_of_stationery = number_of_pens + number_of_pencils
    cost_of_pens = 5
    cost_of_pencils = 4
    total_cost = cost_of_pens * number_of_pens + cost_of_pencils * number_of_pencils
    result = total_cost
    return result

print(solution())