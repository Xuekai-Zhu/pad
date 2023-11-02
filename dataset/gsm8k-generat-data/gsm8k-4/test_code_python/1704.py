def solution():
    """At the salad bar, Grandma put three mushrooms on her salad. She also added twice as many cherry tomatoes as mushrooms, 4 times as many pickles as cherry tomatoes, and 4 times as many bacon bits as pickles. If one third of the bacon bits were red, than how many red bacon bits did Grandma put on her salad?"""
    
    # Calculate the number of cherry tomatoes
    mushrooms = 3
    cherry_tomatoes = mushrooms * 2

    # Calculate the number of pickles
    pickles = cherry_tomatoes * 4

    # Calculate the total number of bacon bits and the number that are red
    bacon_bits = pickles * 4
    red_bacon_bits = bacon_bits / 3

    # Return the number of red bacon bits
    result = red_bacon_bits
    return result

print(solution())