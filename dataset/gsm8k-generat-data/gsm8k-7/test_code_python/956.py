def solution():
    garden_size = 64

    # Calculate the size of the fruit section
    fruit_size = garden_size / 2

    # Calculate the size of the area reserved for strawberries
    strawberry_size = fruit_size / 4
    result = strawberry_size
    return result

print(solution())