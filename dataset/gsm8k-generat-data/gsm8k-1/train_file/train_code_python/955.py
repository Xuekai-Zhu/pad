def solution():
    """Joel’s garden is 64 square feet large. He wants to use half of the garden for fruits and half of the garden for vegetables. He wants to use a quarter of the fruit section for strawberries. How many square feet of the garden will be used for strawberries?"""
    garden_size = 64
    fruit_size = garden_size / 2
    strawberry_size = fruit_size / 4
    result = strawberry_size
    return result

print(solution())