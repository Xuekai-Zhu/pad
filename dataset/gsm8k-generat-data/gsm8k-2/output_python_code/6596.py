def solution():
    """At a recent fishing tournament, Alex caught 7 times as many fish as Jacob. Jacob did not think that he had any chance of winning, but Alex became overconfident and knocked over his bucket of fish, losing 23 fish back to the lake. If Jacob had 8 fish at the beginning, how many more fish does he need to catch to beat Alex by just 1 fish?"""
    jacob_initial_fish = 8
    alex_initial_fish = 7 * jacob_initial_fish
    alex_lost_fish = 23
    alex_final_fish = alex_initial_fish - alex_lost_fish
    jacob_needed_fish = alex_final_fish - jacob_initial_fish + 1
    result = jacob_needed_fish
    return result

print(solution())