def solution():
    """Rob, Royce, and Pedro are contractors getting ready to put a new roof on three homes. If the three homes will need 250 cases of shingles, with the first house needing 1/2 of the second, and the third needing double the first. How many cases of shingles will the third house need?"""
    total_shingles = 250
    second_house = total_shingles / 4
    first_house = second_house / 2
    third_house = first_house * 2
    result = third_house
    return result

print(solution())