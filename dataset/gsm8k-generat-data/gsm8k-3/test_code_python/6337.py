def solution():
    """There are 141 gold balloons and twice as many silver balloons. If the gold and silver balloons were added to 150 black balloons, how many balloons are there in total?"""
    # Define the number of gold balloons and calculate the number of silver balloons
    gold_balloons = 141
    silver_balloons = 2 * gold_balloons

    # Calculate the total number of balloons
    total_balloons = gold_balloons + silver_balloons + 150

    # Display the total number of balloons
    result = total_balloons
    return result

print(solution())