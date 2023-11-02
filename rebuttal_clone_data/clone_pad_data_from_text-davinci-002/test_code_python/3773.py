def solution():
    cherry_flavored = 30
    strawberry_flavored = 40
    pineapple_flavored = 50
    sweets_ eaten = (cherry_flavored + strawberry_flavored + pineapple_flavored) / 2
    sweets_given = 5
    sweets_left = cherry_flavored - sweets_given
    result = sweets_left
    return result

print(solution())