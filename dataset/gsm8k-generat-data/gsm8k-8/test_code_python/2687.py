def solution():
    # Define the initial number of native trees and the multiplier for Monday's planting
    native_trees = 30
    monday_multiplier = 3

    # Calculate the total number of trees after Monday's planting
    monday_total = (native_trees + monday_multiplier * native_trees)

    # Calculate the number of trees planted on Tuesday
    tuesday_planted = monday_total / 3

    # Calculate the total number of trees planted
    total_planted = native_trees + monday_total + tuesday_planted
    result = total_planted
    return result

print(solution())