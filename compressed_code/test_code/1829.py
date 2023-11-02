def solution():
    
    peppers_for_very_spicy = 3 * 30
    peppers_for_spicy = 2 * 30
    peppers_for_mild = 1 * 10
    total_peppers_before = peppers_for_very_spicy + peppers_for_spicy + peppers_for_mild
    peppers_for_spicy = 2 * 15
    peppers_for_mild = 1 * 90
    total_peppers_after = peppers_for_spicy + peppers_for_mild
    fewer_peppers = total_peppers_before - total_peppers_after
    result = fewer_peppers
    return result

print(solution())