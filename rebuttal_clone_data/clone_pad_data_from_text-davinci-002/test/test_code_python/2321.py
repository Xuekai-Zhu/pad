def solution():
     total_cases = 17
     cases_dismissed = 2
     cases_remaining = total_cases - cases_dismissed
     cases_innocent = (cases_remaining / 3) * 2
     cases_delayed = 1
     cases_guilty = cases_remaining - cases_innocent - cases_delayed
     result = cases_guilty
     return result

print(solution())