def solution():
    # Calculate the total number of vegetables already planted
    total_planted = 3*5 + 5*4 + 30  # 3 kinds of tomatoes, 5 of each kind, 5 kinds of cucumbers, 4 of each kind, and 30 potatoes

    # Calculate the total number of spaces available for planting vegetables
    total_spaces = 10*15

    # Calculate the number of more vegetables that could be planted
    more_vegetables = total_spaces - total_planted
    result = more_vegetables
    return result

print(solution())