def solution():
    """Bob is going to put in a vegetable garden on his property. It's going to be in one of the back corners of his land. He wants the width of the garden to be about an eighth of the width of his property, and the length to be a tenth of the length of his property. His land is 1000 feet wide and 2250 feet long. How many square feet is his garden going to be?"""
    width = 1000 * (1/8)
    length = 2250 * (1/10)
    area = width * length
    
    result = area
    return result

print(solution())