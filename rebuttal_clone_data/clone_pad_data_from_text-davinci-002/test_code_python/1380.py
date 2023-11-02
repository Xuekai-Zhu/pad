def solution():
    susy_followers = 100
    sarah_followers = 50
    susy_increase_1 = 40
    susy_increase_2 = susy_increase_1 / 2
    susy_increase_3 = susy_increase_2 / 2
    sarah_increase_1 = 90
    sarah_increase_2 = sarah_increase_1 / 3
    sarah_increase_3 = sarah_increase_2 / 3
    susy_total = susy_followers + susy_increase_1 + susy_increase_2 + susy_increase_3
    sarah_total = sarah_followers + sarah_increase_1 + sarah_increase_2 + sarah_increase_3
    result = max(susy_total, sarah_total)
    return result

print(solution())