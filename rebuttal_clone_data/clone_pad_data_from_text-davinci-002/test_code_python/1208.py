def solution():
 lioness_age = 12
 hyena_age = lioness_age / 2
 lioness_baby_age = lioness_age / 2
 hyena_baby_age = hyena_age / 2
 total_age = lioness_baby_age + hyena_baby_age
 total_age_in_five_years = total_age + 5
 result = total_age_in_five_years
 return result

print(solution())