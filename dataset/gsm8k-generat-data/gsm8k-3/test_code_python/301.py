def solution():
    """Basil gets 1/2 of a dog cookie in the morning and before bed. She gets 2 whole cookies during the day. Basil’s cookies are packaged with 45 cookies per box. How many boxes will she need to last her for 30 days?"""
    # Calculate the total number of cookies Basil gets per day
    cookies_per_day = (1/2) * 2 + 2
    # Calculate the total number of cookies Basil needs for 30 days
    cookies_for_30_days = cookies_per_day * 30
    # Calculate the number of boxes Basil needs, rounding up to the nearest whole number
    boxes_needed = math.ceil(cookies_for_30_days / 45)
    # Display the number of boxes needed
    result = boxes_needed
    return result

print(solution())