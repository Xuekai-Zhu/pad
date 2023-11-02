def solution():
    """Jenna starts out with 8 sapphires. She trades 3 sapphires for two rubies. If sapphires are worth $800 and rubies are worth $1200, how much money are all her jewels worth?"""
    sapphire_value = 800
    ruby_value = 1200
    starting_sapphires = 8
    traded_sapphires = 3
    gained_rubies = 2
    final_sapphires = starting_sapphires - traded_sapphires
    final_rubies = gained_rubies
    total_sapphire_value = final_sapphires * sapphire_value
    total_ruby_value = final_rubies * ruby_value
    total_value = total_sapphire_value + total_ruby_value
    result = total_value
    return result

print(solution())