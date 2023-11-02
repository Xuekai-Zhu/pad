def solution():
    """After Betty gave Stuart 40% of her marble collection, the number of marbles in Stuart's collection increased to 80. If Betty had 60 marbles, how many marbles did Stuart have initially?"""
    betty_marbles = 60
    stuart_marbles = 80
    after_gift = stuart_marbles / 1.4
    initial_marbles = after_gift - betty_marbles
    result = initial_marbles
    return result

print(solution())