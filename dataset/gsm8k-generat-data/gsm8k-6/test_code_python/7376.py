def solution():
    # Calculate the total number of pieces of beef jerky Janette will eat on her trip
    total_jerky_eaten = 5 * (1 + 1 + 2)  # 1 for breakfast, 1 for lunch, and 2 for dinner each day

    # Calculate the number of pieces of beef jerky Janette has left after the trip
    jerky_left = 40 - total_jerky_eaten  

    # Calculate the number of pieces of beef jerky Janette gives to her brother
    jerky_given_away = jerky_left / 2  

    # Calculate the number of pieces of beef jerky Janette has left after giving some to her brother
    jerky_left_after_gift = jerky_left - jerky_given_away  

    result = jerky_left_after_gift
    return result

print(solution())