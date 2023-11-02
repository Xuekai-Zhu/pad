def solution():
    """After Betty gave Stuart 40% of her marble collection, the number of marbles in Stuart's collection increased to 80. If Betty had 60 marbles, how many marbles did Stuart have initially?"""
    betty_marbles = 60
    stuart_increase = 80 - betty_marbles
    stuart_percent = 40
    stuart_initial = (stuart_increase / (stuart_percent / 100)) + betty_marbles
    result = stuart_initial
    return result

print(solution())