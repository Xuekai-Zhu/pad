def solution():
    cereal_box1 = 14  # First cereal box holds 14 ounces of cereal
    cereal_box2 = cereal_box1 / 2  # Second cereal box holds half the amount of the first box
    cereal_box3 = cereal_box2 + 5  # Third cereal box holds 5 ounces less than the second box

    # Calculate total cereal amount in all 3 boxes
    total_cereal = cereal_box1 + cereal_box2 + cereal_box3
    result = total_cereal
    return result

print(solution())