def solution():
    """Lucille is wondering who has the tallest house between her and her neighbors. His family's house is 80 feet tall. One neighbor's house is 70 feet tall. Another neighbor's house is 99 feet tall. How much shorter is Lucille's house than the average height?"""
    # Define the heights of the houses
    lucille_height = 80
    neighbor1_height = 70
    neighbor2_height = 99

    # Calculate the average height
    avg_height = (lucille_height + neighbor1_height + neighbor2_height) / 3

    # Calculate how much shorter Lucille's house is than the average height
    diff_height = avg_height - lucille_height

    # Display the result
    result = diff_height
    return result

print(solution())