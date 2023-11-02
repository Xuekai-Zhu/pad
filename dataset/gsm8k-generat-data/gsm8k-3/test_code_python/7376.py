def solution():
    """Janette went camping for 5 days. She brought along 40 pieces of beef jerky. She wants to ration it out so that she can eat 1 for breakfast, 1 for lunch, and 2 for dinner each day. When she returns from the trip, she plans on giving half of the remaining pieces to her brother. How many pieces of beef jerky will she have left once she does this?"""
    # Calculate the total number of pieces of jerky Janette needs per day
    pieces_per_day = 1 + 1 + 2

    # Calculate the total number of pieces of jerky Janette needs for the whole trip
    total_pieces_needed = pieces_per_day * 5

    # Calculate the number of pieces of jerky left after the trip
    pieces_left = 40 - total_pieces_needed

    # Calculate the number of pieces of jerky Janette gives to her brother
    pieces_given_away = pieces_left / 2

    # Calculate the number of pieces of jerky left after giving half to her brother
    pieces_left = pieces_left - pieces_given_away

    # Display the final number of pieces of jerky left
    result = pieces_left
    return result

print(solution())