def solution():
    """A certain tree was 100 meters tall at the end of 2017. It will grow 10% more than its previous height each year. How long has the tree grown from 2017 until the end of 2019?"""
    height_2017 = 100
    height_2018 = height_2017 + (height_2017 * 0.1)
    height_2019 = height_2018 + (height_2018 * 0.1)
    total_growth = height_2019 - height_2017
    result = total_growth
    return result

print(solution())