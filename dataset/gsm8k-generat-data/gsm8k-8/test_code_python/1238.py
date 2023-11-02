def solution():
    # Define the amount of cereal in each box
    box1_cereal = 14
    box2_cereal = box1_cereal / 2
    box3_cereal = box2_cereal + 5

    # Calculate the total amount of cereal
    total_cereal = box1_cereal + box2_cereal + box3_cereal
    result = total_cereal
    return result

print(solution())