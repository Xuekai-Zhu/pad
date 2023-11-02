def solution():
    """Roman the Tavernmaster has $20 worth of gold coins. He sells 3 gold coins to Dorothy. After she pays him, he has $12. How many gold coins does Roman have left?"""
    roman_coins = 20
    dorothy_coins = 3
    roman_coins -= dorothy_coins

    roman_coins_value = 12
    roman_coins_value -= (dorothy_coins * 4)
    roman_coins_left = roman_coins_value / 2
    result = roman_coins_left
    return result

print(solution())