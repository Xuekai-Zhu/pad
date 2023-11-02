def solution():
    total_granola_bars = 200
    eaten_by_monroe_and_husband = 80
    granola_bars_given_to_children = total_granola_bars - eaten_by_monroe_and_husband
    number_of_children = granola_bars_given_to_children / 20
    result = number_of_children
    return result

print(solution())