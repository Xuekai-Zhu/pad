def solution():
    # Find the number of stuffed animals sold by Thor
    thor = (200/10) - 10  # Quincy sold ten times as many stuffed animals as Thor, and Jake sold 10 more than Thor.

    # Find the number of stuffed animals sold by Jake
    jake = thor + 10  

    # Find the difference in the number of stuffed animals sold by Quincy and Jake
    difference = 200 - jake  

    result = difference
    return result

print(solution())