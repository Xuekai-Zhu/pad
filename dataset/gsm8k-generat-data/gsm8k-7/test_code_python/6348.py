def solution():
    num_singles = 9
    num_twins = 5
    traded_calves = 8
    traded_adults = 2

    # Calculate the total number of calves born
    total_calves = num_singles + (num_twins * 2)

    # Calculate the total number of adult llamas after trading
    total_adults = traded_adults + (traded_calves - 8)

    # Calculate the total number of llamas before selling
    total_llamas_before_selling = total_calves + total_adults

    # Calculate the number of llamas to sell
    num_to_sell = total_llamas_before_selling / 3

    # Calculate the number of llamas remaining after selling
    total_llamas_now = total_llamas_before_selling - num_to_sell
    result = total_llamas_now
    return result

print(solution())