def solution():
    father_dig_rate = 4
    father_dig_time = 400
    father_hole_depth = father_dig_rate * father_dig_time
    son_hole_depth = father_hole_depth / 2 - 400
    son_dig_time = son_hole_depth / father_dig_rate
    result = son_dig_time
    return result

print(solution())