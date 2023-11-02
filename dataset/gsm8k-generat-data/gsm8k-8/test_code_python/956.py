def solution():
    # Calculate the total area of the garden
    total_area = 64

    # Calculate the area for fruits and vegetables (half of total area each)
    fruit_area = total_area / 2
    veggie_area = total_area / 2

    # Calculate the area for strawberries (a quarter of the fruit area)
    strawberry_area = fruit_area / 4
    result = strawberry_area
    return result

print(solution())