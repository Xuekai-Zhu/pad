def solution():
    """Janeth bought 5 bags of round balloons with 20 balloons in each bag. She also bought 4 bags of long balloons with 30 balloons in each bag. While blowing up the balloons, 5 round balloons burst. How many balloons are left?"""
    # Calculate the total number of balloons
    total_balloons = (5 * 20) + (4 * 30)

    # Subtract the number of burst round balloons
    total_balloons -= 5

    # Display the number of remaining balloons
    result = total_balloons
    return result

print(solution())