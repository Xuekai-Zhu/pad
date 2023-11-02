def solution():
    """Janette went camping for 5 days. She brought along 40 pieces of beef jerky. She wants to ration it out so that she can eat 1 for breakfast, 1 for lunch, and 2 for dinner each day. When she returns from the trip, she plans on giving half of the remaining pieces to her brother. How many pieces of beef jerky will she have left once she does this?"""
    # Define the initial number of beef jerky pieces
    beef_jerky = 40

    # Calculate the number of beef jerky pieces consumed each day
    daily_consumption = 1 + 1 + 2
    total_consumption = daily_consumption * 5

    # Calculate the remaining beef jerky pieces
    remaining = beef_jerky - total_consumption

    # Calculate the number of beef jerky pieces given to her brother
    given_away = remaining / 2

    # Calculate the final number of beef jerky pieces remaining
    final_remaining = remaining - given_away

    # Return the result
    result = final_remaining
    return result

print(solution())