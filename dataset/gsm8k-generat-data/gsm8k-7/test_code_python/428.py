def solution():
    first_day_eggs = 50
    second_day_eggs = first_day_eggs * 2
    third_day_eggs = second_day_eggs + 20
    total_eggs = first_day_eggs + second_day_eggs + third_day_eggs + (first_day_eggs + second_day_eggs + third_day_eggs) * 2
    result = total_eggs
    return result

print(solution())