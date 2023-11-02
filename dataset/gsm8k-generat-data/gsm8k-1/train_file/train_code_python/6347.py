def solution():
    """Jill runs a business breeding llamas. Nine of her llamas got pregnant with 1 calf, and 5 of them got pregnant with twins. After they give birth, Jill traded 8 of the calves for 2 new adult llamas. Then she sells 1/3 of her herd at the market. How many total llamas (calves and adults) does Jill have now?"""
    pregnant_llamas = 9 + (5*2)
    calves = 9 + (5*2*2)
    adult_llamas = 0 + 2
    total_llamas = pregnant_llamas + calves + adult_llamas
    sold_llamas = total_llamas // 3
    remaining_llamas = total_llamas - sold_llamas
    result = remaining_llamas
    return result

print(solution())