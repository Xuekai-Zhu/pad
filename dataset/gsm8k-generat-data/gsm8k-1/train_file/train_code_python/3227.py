def solution():
    """For breakfast, Daisy bought a muffin for $2 and a cup of coffee for $4. For lunch, Daisy had soup, a salad, and lemonade. The soup cost $3, the salad cost $5.25, and the lemonade cost $0.75. How much more money did Daisy spend on lunch than on breakfast?"""
    breakfast_total = 2 + 4
    lunch_total = 3 + 5.25 + 0.75
    difference = lunch_total - breakfast_total
    result = difference
    return result

print(solution())