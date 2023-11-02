def solution():
    # Calculate the total number of blue marbles Janelle bought
    blue_marbles = 6 * 10  # each bag has 10 blue marbles

    # Calculate the total number of marbles Janelle had before giving the gift
    total_marbles = 26 + blue_marbles  # Janelle had 26 green marbles

    # Calculate the total number of marbles Janelle has now
    remaining_green_marbles = 26 - 6  # Janelle gave 6 green marbles as gift
    remaining_blue_marbles = blue_marbles - 8  # Janelle gave 8 blue marbles as gift
    final_total_marbles = remaining_green_marbles + remaining_blue_marbles

    result = final_total_marbles
    return result

print(solution())