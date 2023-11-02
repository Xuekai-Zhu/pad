def solution():
    """Lucille is wondering who has the tallest house between her and her neighbors. His family's house is 80 feet tall. One neighbor's house is 70 feet tall. Another neighbor's house is 99 feet tall. How much shorter is Lucille's house than the average height?"""
    lucille_house = 80
    neighbor1_house = 70
    neighbor2_house = 99

    average_height = (lucille_house + neighbor1_house + neighbor2_house) / 3
    difference = average_height - lucille_house

    result = difference
    return result

print(solution())