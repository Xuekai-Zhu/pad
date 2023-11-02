def solution():
    """A party store ordered 5 boxes of balloons. Each box contains 8 bags of balloons, and there are 12 balloons in each bag. How many balloons are there?"""
    # Define the number of boxes, bags, and balloons per bag
    BOXES = 5
    BAGS_PER_BOX = 8
    BALLOONS_PER_BAG = 12

    # Calculate the total number of balloons
    total_balloons = BOXES * BAGS_PER_BOX * BALLOONS_PER_BAG

    # Display the total number of balloons
    result = total_balloons
    return result

print(solution())