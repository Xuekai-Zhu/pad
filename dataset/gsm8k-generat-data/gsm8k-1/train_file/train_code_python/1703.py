def solution():
    """At the salad bar, Grandma put three mushrooms on her salad. She also added twice as many cherry tomatoes as mushrooms, 4 times as many pickles as cherry tomatoes, and 4 times as many bacon bits as pickles. If one third of the bacon bits were red, than how many red bacon bits did Grandma put on her salad?"""
    mushrooms = 3
    cherry_tomatoes = 2 * mushrooms
    pickles = 4 * cherry_tomatoes
    bacon_bits = 4 * pickles
    red_bacon_bits = bacon_bits / 3
    result = red_bacon_bits
    return result

print(solution())