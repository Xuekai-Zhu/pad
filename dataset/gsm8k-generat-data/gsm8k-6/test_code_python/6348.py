def solution():
    # Calculate the initial number of llamas
    initial_lamas = 9 + 5*2  # 9 llamas pregnant with 1 calf, 5 llamas pregnant with twins

    # Calculate the number of llamas after trading 8 calves
    traded_calves = 8
    remaining_calves = initial_lamas - traded_calves
    adult_llamas_after_trade = 2
    total_llamas_after_trade = remaining_calves + adult_llamas_after_trade

    # Calculate the number of llamas after selling 1/3 of the herd
    sold_lamas = total_llamas_after_trade / 3
    remaining_lamas = total_llamas_after_trade - sold_lamas
    result = remaining_lamas
    return result

print(solution())