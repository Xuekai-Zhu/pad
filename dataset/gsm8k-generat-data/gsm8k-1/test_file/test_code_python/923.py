def solution():
    """Andrew bakes 200 mini cinnamon rolls and 300 mini blueberry muffins. A normal cinnamon roll has 600 calories and a normal blueberry muffin has 450 calories. If a mini pastry has 1/3rd of the calories of a normal version, how many calories do the pastries he baked have?"""
    cinnamon_cal = 600
    blueberry_cal = 450
    mini_cal = 1/3
    cinnamon_total = 200 * cinnamon_cal * mini_cal
    blueberry_total = 300 * blueberry_cal * mini_cal
    total_calories = cinnamon_total + blueberry_total
    result = total_calories
    return result

print(solution())