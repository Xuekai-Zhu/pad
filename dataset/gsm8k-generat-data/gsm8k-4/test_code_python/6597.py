def solution():
    """At a recent fishing tournament, Alex caught 7 times as many fish as Jacob. Jacob did not think that he had any chance of winning, but Alex became overconfident and knocked over his bucket of fish, losing 23 fish back to the lake. If Jacob had 8 fish at the beginning, how many more fish does he need to catch to beat Alex by just 1 fish?"""
    # Define the initial number of fish caught by Jacob and Alex
    jacob_fish = 8
    alex_fish = jacob_fish * 7

    # Calculate how many fish Alex has after losing some to the lake
    alex_fish -= 23

    # Calculate how many fish Jacob needs to beat Alex by just 1 fish
    fish_needed = alex_fish - jacob_fish + 1

    result = fish_needed
    return result

print(solution())