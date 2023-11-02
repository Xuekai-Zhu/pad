def solution():
    # Calculate the number of calves born
    calves = 9 + (5*2)  # 9 llamas had 1 calf, 5 llamas had twins

    # Calculate the number of adult llamas after the trade
    adult_llamas = 2 + 9  # Jill traded 8 calves for 2 adult llamas, and had 9 to begin with

    # Calculate the total number of llamas before selling
    total_llamas = calves + adult_llamas

    # Calculate the number of llamas sold
    sold_llamas = total_llamas // 3

    # Calculate the total number of llamas remaining
    remaining_llamas = total_llamas - sold_llamas

    result = remaining_llamas
    return result

print(solution())