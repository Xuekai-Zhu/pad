def solution():
    painting_area = 2*4  # The painting has an area of 2 feet by 4 feet
    wall_area = 5*10  # The wall has an area of 5 feet by 10 feet

    # Calculate the percentage of the wall taken up by the painting
    percentage = (painting_area/wall_area) * 100
    result = percentage
    return result

print(solution())