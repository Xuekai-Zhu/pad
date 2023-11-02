def solution():
    """Ali is collecting bottle caps. He has 125 bottle caps. He has red ones and green ones. If he has 50 red caps, what percentage of caps are green?"""
    total_caps = 125
    red_caps = 50
    green_caps = total_caps - red_caps
    green_percentage = (green_caps / total_caps) * 100
    result = green_percentage
    return result

print(solution())