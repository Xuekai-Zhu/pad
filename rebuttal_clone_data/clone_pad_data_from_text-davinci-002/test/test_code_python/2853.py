def solution():
     lollipops_start = 42
     lollipops_given_away = lollipops_start * (2/3)
     lollipops_kept = 4
     lollipops_given_to_lou = lollipops_start - lollipops_given_away - lollipops_kept
     result = lollipops_given_to_lou
     return result

print(solution())