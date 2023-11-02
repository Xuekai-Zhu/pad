def solution():
    """Jill runs a business breeding llamas. Nine of her llamas got pregnant with 1 calf, and 5 of them got pregnant with twins. After they give birth, Jill traded 8 of the calves for 2 new adult llamas. Then she sells 1/3 of her herd at the market. How many total llamas (calves and adults) does Jill have now?"""
    # Define the number of llamas that got pregnant with 1 calf and the number of llamas that got pregnant with twins
    SINGLE_BIRTH = 9
    TWIN_BIRTH = 5

    # Calculate the number of calves born
    total_calves = SINGLE_BIRTH + (TWIN_BIRTH * 2)

    # Calculate the number of adult llamas before the trade
    adult_llamas = SINGLE_BIRTH + TWIN_BIRTH

    # Calculate the number of adult llamas after the trade
    adult_llamas += 2

    # Calculate the total number of llamas before selling at the market
    total_llamas = adult_llamas + total_calves

    # Calculate the number of llamas Jill sells at the market
    sold_llamas = round(total_llamas / 3)

    # Calculate the number of llamas Jill has now
    remaining_llamas = total_llamas - sold_llamas

    # Display the total number of llamas Jill has now
    result = remaining_llamas
    return result

print(solution())