def solution():
    # Calculate the total number of calves
    total_calves = 9 + 2 * 5

    # Calculate the number of adult llamas before the trade
    adult_llamas_before_trade = 9 + 5 + 2

    # Calculate the number of adult llamas after the trade
    adult_llamas_after_trade = 2 + 8 - total_calves

    # Calculate the total number of llamas after the trade
    total_llamas_after_trade = adult_llamas_after_trade + total_calves

    # Calculate the number of llamas Jill sells at the market
    sold_llamas = total_llamas_after_trade // 3

    # Calculate the final number of llamas Jill has
    final_total_llamas = total_llamas_after_trade - sold_llamas

    result = final_total_llamas
    return result

print(solution())