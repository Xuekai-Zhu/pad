def solution():
    """Carly had 42 lollipops to share with her friends. Half of the lollipops were cherry, and the rest were equal amounts of watermelon, sour apple, and grape. How many lollipops were grape?"""
    total_lollipops = 42
    cherry_lollipops = total_lollipops / 2
    other_lollipops = total_lollipops - cherry_lollipops
    grape_lollipops = other_lollipops / 3
    result = grape_lollipops
    return result

print(solution())