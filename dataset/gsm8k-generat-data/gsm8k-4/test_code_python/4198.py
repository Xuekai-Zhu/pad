def solution():
    """A party store ordered 5 boxes of balloons. Each box contains 8 bags of balloons, and there are 12 balloons in each bag. How many balloons are there?"""
    # Define the number of boxes, bags, and balloons per bag
    boxes = 5
    bags_per_box = 8
    balloons_per_bag = 12

    # Calculate the total number of balloons
    total_balloons = boxes * bags_per_box * balloons_per_bag

    # return the result
    result = total_balloons
    return result

print(solution())