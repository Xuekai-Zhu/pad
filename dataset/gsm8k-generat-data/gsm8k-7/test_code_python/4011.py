def solution():
    painting_area = 2 * 4  # area of painting in square feet
    wall_area = 5 * 10  # area of wall in square feet

    # Calculate the percentage of wall taken up by the painting
    percentage = (painting_area / wall_area) * 100

    result = percentage
    return result

print(solution())