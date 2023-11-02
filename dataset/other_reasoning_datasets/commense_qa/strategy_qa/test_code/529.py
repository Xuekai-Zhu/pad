def solution():
    number_of_inventions_patented = 3
    self_pasting_scrapbook_creations_sold = 25000
    improvement_in_straps_invented = True
    if number_of_inventions_patented > 0 or self_pasting_scrapbook_creations_sold > 0 or improvement_in_straps_invented:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())