def solution():
    """Basil gets 1/2 of a dog cookie in the morning and before bed. She gets 2 whole cookies during the day. Basil’s cookies are packaged with 45 cookies per box. How many boxes will she need to last her for 30 days?"""
    # Define the number of cookies consumed by Basil each day
    daily_cookies = 1/2 + 1/2 + 2
    # Calculate the total number of cookies needed for 30 days
    total_cookies = daily_cookies * 30
    # Calculate the number of boxes needed
    boxes_needed = total_cookies / 45
    # Round up to the nearest whole number of boxes
    result = math.ceil(boxes_needed)
    return result

print(solution())