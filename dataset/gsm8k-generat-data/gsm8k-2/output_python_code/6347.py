def solution():
    """Jill runs a business breeding llamas. Nine of her llamas got pregnant with 1 calf, and 5 of them got pregnant with twins. After they give birth, Jill traded 8 of the calves for 2 new adult llamas. Then she sells 1/3 of her herd at the market. How many total llamas (calves and adults) does Jill have now?"""
    single_calf_lamas = 9
    twin_calf_lamas = 5
    total_calf_lamas = single_calf_lamas + (2 * twin_calf_lamas)
    traded_calves = 8
    traded_adults = 2
    remaining_calves = total_calf_lamas - traded_calves
    total_adults = traded_adults + remaining_calves
    total_llamas = total_adults + total_calf_lamas
    sold_fraction = 1/3
    remaining_llamas = total_llamas - (total_llamas * sold_fraction)
    result = remaining_llamas
    return result

print(solution())