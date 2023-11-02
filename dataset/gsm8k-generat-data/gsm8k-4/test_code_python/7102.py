def solution():
    """Bob is going to put in a vegetable garden on his property. It's going to be in one of the back corners of his land. He wants the width of the garden to be about an eighth of the width of his property, and the length to be a tenth of the length of his property. His land is 1000 feet wide and 2250 feet long. How many square feet is his garden going to be?"""
    # Define the width and length of the garden
    garden_width = 1000 / 8
    garden_length = 2250 / 10

    # Calculate the area of the garden
    garden_area = garden_width * garden_length

    # Return the result
    result = garden_area
    return result

print(solution())