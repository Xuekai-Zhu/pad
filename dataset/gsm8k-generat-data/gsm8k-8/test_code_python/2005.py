def solution():
    # Calculate the total number of cups before giving away any to the construction crew
    total_cups = 2 * 18

    # Calculate the number of cups sold to the construction crew
    construction_crew_cups = total_cups / 2

    # Calculate the number of cups left after selling to the construction crew
    remaining_cups = total_cups - construction_crew_cups

    # Calculate the number of cups given away to friends
    friend_cups = 18 / 2

    # Calculate the final number of cups
    final_cups = remaining_cups - friend_cups - 1 #accounting for Hazel's one cup
    result = final_cups
    return result

print(solution())