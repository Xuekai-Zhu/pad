def solution():
    """Joel’s garden is 64 square feet large. He wants to use half of the garden for fruits and half of the garden for vegetables. He wants to use a quarter of the fruit section for strawberries. How many square feet of the garden will be used for strawberries?"""
    # Define the size of the garden
    garden_size = 64

    # Calculate the size of the fruit section and the vegetable section
    fruit_size = garden_size / 2
    veggie_size = garden_size / 2

    # Calculate the size of the strawberry section
    strawberry_size = fruit_size / 4

    # Return the result
    result = strawberry_size
    return result

print(solution())