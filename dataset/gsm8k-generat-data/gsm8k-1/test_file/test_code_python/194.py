def solution():
    """Elaine initially had 20 Pokemon cards. After a month, she collected three times that number. In the second month, she collected 20 fewer cards than those she collected in the first month. In the third month, she collected twice the combined number of pokemon cards she collected in the first and second months. How many pokemon cards does she have now in total?"""
    initial_cards = 20
    first_month_cards = initial_cards * 3
    second_month_cards = first_month_cards - 20
    third_month_cards = 2 * (initial_cards + first_month_cards + second_month_cards)
    total_cards = initial_cards + first_month_cards + second_month_cards + third_month_cards
    result = total_cards
    return result

print(solution())