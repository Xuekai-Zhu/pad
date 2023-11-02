def solution():
    total_prizes = 800
    first_place = 200
    second_place = 150
    third_place = 120
    fourth_place = (total_prizes - (first_place + second_place + third_place)) / 15
    result = fourth_place
    return result

print(solution())