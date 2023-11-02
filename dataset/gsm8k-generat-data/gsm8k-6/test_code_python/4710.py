def solution():
    # Calculate the distance between Arizona and Missouri
    arizona_to_missouri = 2000 / 2  # Missouri is midway between Arizona and New York

    # Calculate the distance between Missouri and New York if driven
    missouri_to_newyork = arizona_to_missouri * 1.4  # the distance between the 2 states increases by 40% if driven

    result = missouri_to_newyork
    return result

print(solution())