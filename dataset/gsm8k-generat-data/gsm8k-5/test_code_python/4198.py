def solution():
    boxes = 5  # The party store ordered 5 boxes of balloons
    bags_per_box = 8  # Each box contains 8 bags of balloons
    balloons_per_bag = 12  # There are 12 balloons in each bag

    # Calculate the total number of balloons
    total_balloons = boxes * bags_per_box * balloons_per_bag
    result = total_balloons
    return result

print(solution())