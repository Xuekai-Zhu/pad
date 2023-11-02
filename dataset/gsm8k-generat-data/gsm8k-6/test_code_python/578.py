def solution():
    # Calculate the total earnings from catching fish on Sunday
    trout = 0.6 * 5  # 60% were trout
    blue_gill = 5 - trout  # the rest were blue-gill
    earnings = (trout * 5) + (blue_gill * 4)

    # Calculate the total amount of money Bucky has saved
    total_earnings = 35 + earnings

    # Calculate how much more he needs to save for the game
    remaining_money = 60 - total_earnings
    result = remaining_money
    return result

print(solution())