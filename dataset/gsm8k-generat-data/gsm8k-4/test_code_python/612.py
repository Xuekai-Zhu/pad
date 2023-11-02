def solution():
    """Ali is collecting bottle caps. He has 125 bottle caps. He has red ones and green ones. If he has 50 red caps, what percentage of caps are green?"""
    # Define the number of red and total caps
    red_caps = 50
    total_caps = 125

    # Calculate the number of green caps
    green_caps = total_caps - red_caps

    # Calculate the percentage of green caps
    green_percentage = (green_caps / total_caps) * 100

    # return the result
    result = green_percentage
    return result

print(solution())