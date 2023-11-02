def solution():
    """5 geckos on the kitchen window eat 6 insects each. 3 lizards eat twice as much as the geckos. How many total insects were eaten?"""
    gecko_count = 5
    gecko_insects = 6
    lizard_count = 3
    lizard_insects = gecko_insects * 2
    total_insects = (gecko_count * gecko_insects) + (lizard_count * lizard_insects)
    result = total_insects
    return result

print(solution())