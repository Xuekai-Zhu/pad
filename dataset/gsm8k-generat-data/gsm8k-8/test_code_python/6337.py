def solution():
    # Define the number of gold balloons
    gold_balloons = 141

    # Calculate the number of silver balloons using the ratio
    silver_balloons = 2 * gold_balloons

    # Calculate the total number of balloons
    total_balloons = gold_balloons + silver_balloons + 150
    result = total_balloons
    return result

print(solution())