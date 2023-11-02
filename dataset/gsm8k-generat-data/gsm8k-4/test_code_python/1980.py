def solution():
    """Janeth bought 5 bags of round balloons with 20 balloons in each bag. She also bought 4 bags of long balloons with 30 balloons in each bag. While blowing up the balloons, 5 round balloons burst. How many balloons are left?"""
    # Define the initial number of balloons
    initial_balloons = 5 * 20 + 4 * 30

    # Calculate the number of balloons after bursting
    remaining_balloons = initial_balloons - 5

    result = remaining_balloons
    return result

print(solution())