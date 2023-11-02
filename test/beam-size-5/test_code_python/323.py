def solution():
    
    initial_lollipops = 24
    lollipops_to_school = 2
    lollipops_given_away = 14
    lollipops_bought = lollipops_to_school * 2
    lollipops_in_morning = lollipops_bought + 3 + 2
    total_lollipops = initial_lollipops - lollipops_to_school - lollipops_bought - lollipops_in_morning
    result = total_lollipops
    return result

print(solution())