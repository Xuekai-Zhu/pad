def solution():
    apples_in_four_bags = 4 * 20
    apples_in_six_bags = 6 * 25
    total_apples = apples_in_four_bags + apples_in_six_bags
    apples_sold = 200
    apples_left = total_apples - apples_sold
    result = apples_left
    return result

print(solution())