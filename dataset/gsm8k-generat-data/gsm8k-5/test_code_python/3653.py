def solution():
    boxes = 4  # Mrs. Jackson has 4 boxes of Christmas decorations
    decorations_per_box = 15  # There are 15 decorations in each box
    total_decorations = boxes * decorations_per_box  # Calculate the total number of decorations
    used_decorations = 35  # Mrs. Jackson was only able to use 35 decorations
    given_away_decorations = total_decorations - used_decorations  # Calculate the number of decorations given away
    result = given_away_decorations
    return result

print(solution())