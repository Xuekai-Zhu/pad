def solution():
    # Set the year England won any Olympic gold medal 
    england_gold_year = 0
    # The Olympics were first held in 1896, so England couldn't have won a gold medal in 1800
    if england_gold_year < 1896:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())