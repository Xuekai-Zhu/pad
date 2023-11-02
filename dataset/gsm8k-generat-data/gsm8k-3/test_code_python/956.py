def solution():
    """Joel’s garden is 64 square feet large. He wants to use half of the garden for fruits and half of the garden for vegetables. He wants to use a quarter of the fruit section for strawberries. How many square feet of the garden will be used for strawberries?"""
    # Define the area of the garden
    garden_area = 64

    # Calculate the area of the fruit section
    fruit_area = garden_area / 2

    # Calculate the area of the strawberry section
    strawberry_area = fruit_area / 4

    # Display the area of the strawberry section
    result = strawberry_area
    return result

print(solution())