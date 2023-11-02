def solution():
    """Janette went camping for 5 days. She brought along 40 pieces of beef jerky. She wants to ration it out so that she can eat 1 for breakfast, 1 for lunch, and 2 for dinner each day. When she returns from the trip, she plans on giving half of the remaining pieces to her brother. How many pieces of beef jerky will she have left once she does this?"""
    days = 5
    total_jerky = 40
    daily_jerky = 1 + 1 + 2
    jerky_consumed = days * daily_jerky
    jerky_remaining = total_jerky - jerky_consumed
    jerky_given = jerky_remaining / 2
    jerky_left = jerky_remaining - jerky_given
    result = jerky_left
    return result

print(solution())