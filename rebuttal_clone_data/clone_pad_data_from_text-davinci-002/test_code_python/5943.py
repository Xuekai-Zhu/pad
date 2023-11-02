def solution():
    total_lollipops = 42
    cherry_lollipops = total_lollipops / 2
    watermelon_lollipops = (total_lollipops - cherry_lollipops) / 3
    grape_lollipops = total_lollipops - cherry_lollipops - watermelon_lollipops
    result = grape_lollipops
    
    return result

print(solution())