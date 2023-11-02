def solution():
    
    peppers_for_very_spicy_curries = 30 * 3
    peppers_for_spicy_curries = 30 * 2
    peppers_for_mild_curries = 10 * 1
    
    peppers_needed_for_spicy_curries = 15 * 2
    peppers_needed_for_mild_curries = 90 * 1
    
    total_peppers_bought_before = peppers_for_very_spicy_curries + peppers_for_spicy_curries + peppers_for_mild_curries
    total_peppers_bought_after = peppers_needed_for_spicy_curries + peppers_needed_for_mild_curries
    
    difference = total_peppers_bought_before - total_peppers_bought_after
    
    result = difference
    return result

print(solution())