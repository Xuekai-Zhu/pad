def solution():
    fish_needed = 40
    fish_bought = 400
    fish_gone_bad = fish_bought * 0.2
    fish_used = fish_bought - fish_gone_bad
    sushi_rolls = fish_used // fish_needed
    result = sushi_rolls
    return result

print(solution())