def solution():
    """Janette went camping for 5 days. She brought along 40 pieces of beef jerky. She wants to ration it out so that she can eat 1 for breakfast, 1 for lunch, and 2 for dinner each day. When she returns from the trip, she plans on giving half of the remaining pieces to her brother. How many pieces of beef jerky will she have left once she does this?"""
    days = 5
    breakfast = 1
    lunch = 1
    dinner = 2
    daily_jerky = breakfast + lunch + dinner
    total_jerky_needed = days * daily_jerky
    remaining_jerky = 40 - total_jerky_needed
    jerky_for_brother = remaining_jerky / 2
    remaining_jerky -= jerky_for_brother
    result = remaining_jerky
    return result

print(solution())