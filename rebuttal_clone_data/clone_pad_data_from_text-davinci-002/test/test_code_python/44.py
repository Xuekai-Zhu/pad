def solution():
    
    cans_purchased_by_jennifer = 40
    cans_purchased_by_mark = 50
    cans_bought_per_5_cans_bought_by_mark = 6
    total_cans_purchased_by_jennifer = cans_purchased_by_jennifer + ((cans_purchased_by_mark / 5) * cans_bought_per_5_cans_bought_by_mark)
    result = total_cans_purchased_by_jennifer
    return result

print(solution())