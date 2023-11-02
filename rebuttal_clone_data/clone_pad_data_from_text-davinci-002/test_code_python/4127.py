def solution():
    first_day_daisies = 45
    second_day_daisies = first_day_daisies + 20
    third_day_daisies = (second_day_daisies * 2) - 10
    fourth_day_daisies = 350 - (first_day_daisies + second_day_daisies + third_day_daisies)
    result = fourth_day_daisies
    return result

print(solution())