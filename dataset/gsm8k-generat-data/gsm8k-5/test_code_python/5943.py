def solution():
    total_lollipops = 42  # Carly had 42 lollipops in total
    cherry_lollipops = total_lollipops / 2  # Half of the lollipops were cherry
    remaining_lollipops = total_lollipops - cherry_lollipops  # The remaining lollipops are watermelon, sour apple and grape
    grape_lollipops = remaining_lollipops / 3  # The remaining lollipops are split equally between watermelon, sour apple, and grape
    result = grape_lollipops
    return result

print(solution())