def solution():
    """There are 141 gold balloons and twice as many silver balloons. If the gold and silver balloons were added to 150 black balloons, how many balloons are there in total?"""
    # Define the number of gold balloons
    gold_balloons = 141

    # Calculate the number of silver balloons
    silver_balloons = gold_balloons * 2

    # Define the number of black balloons and calculate the total number of balloons
    black_balloons = 150
    total_balloons = gold_balloons + silver_balloons + black_balloons

    # return the result
    result = total_balloons
    return result

print(solution())