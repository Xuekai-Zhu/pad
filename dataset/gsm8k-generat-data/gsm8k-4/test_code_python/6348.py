def solution():
    """Jill runs a business breeding llamas. Nine of her llamas got pregnant with 1 calf, and 5 of them got pregnant with twins. After they give birth, Jill traded 8 of the calves for 2 new adult llamas. Then she sells 1/3 of her herd at the market. How many total llamas (calves and adults) does Jill have now?"""
    # Define the initial number of llamas
    initial_llamas = 9 + 5*2

    # Define the number of calves and adults after trading
    calves = initial_llamas * 2
    adults = initial_llamas + 2 - 8

    # Calculate the number of llamas after selling 1/3 of them
    total_llamas = int((calves + adults) * (2/3))

    # Return the result
    result = total_llamas
    return result

print(solution())