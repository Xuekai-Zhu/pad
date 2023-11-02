def solution():
    mushrooms = 3  # Grandma put 3 mushrooms on her salad
    cherry_tomatoes = mushrooms * 2  # Grandma added twice as many cherry tomatoes as mushrooms
    pickles = cherry_tomatoes * 4  # Grandma added 4 times as many pickles as cherry tomatoes
    bacon_bits = pickles * 4  # Grandma added 4 times as many bacon bits as pickles

    red_bacon_bits = bacon_bits / 3  # One third of the bacon bits were red

    result = red_bacon_bits
    return result

print(solution())