def solution():
    """How many legs does a spider have if it has two times more than double the number of legs a human has?"""
    human_legs = 2
    spider_legs = 2 * (2 * human_legs) + 2
    result = spider_legs
    return result

print(solution())