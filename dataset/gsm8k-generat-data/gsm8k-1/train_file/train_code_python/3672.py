def solution():
    """Lucille is wondering who has the tallest house between her and her neighbors. His family's house is 80 feet tall. One neighbor's house is 70 feet tall. Another neighbor's house is 99 feet tall. How much shorter is Lucille's house than the average height?"""
    lucille_height = 80
    neighbor1_height = 70
    neighbor2_height = 99
    total_height = lucille_height + neighbor1_height + neighbor2_height
    average_height = total_height / 3
    height_difference = average_height - lucille_height
    result = height_difference
    return result

print(solution())