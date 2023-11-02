def solution():
    # Calculate the total amount of money Lindsey saved
    total_saved = 50 + 37 + 11

    # Check if Lindsey saved more than $75 and add $25 if she did
    if total_saved > 75:
        total_saved += 25

    # Calculate how much money Lindsey has left after buying the video game
    money_left = total_saved - 87
    result = money_left
    return result

print(solution())