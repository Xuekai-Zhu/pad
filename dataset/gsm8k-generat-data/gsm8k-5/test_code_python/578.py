def solution():
    # Calculate the money earned from catching fish on Sunday
    num_trout = 0.6 * 5  # 60% of 5 fish are trout
    num_bluegill = 5 - num_trout  # The rest are blue-gill
    money_earned_sunday = (num_trout * 5) + (num_bluegill * 4)  # $5 earned from each trout, $4 from each blue-gill

    # Calculate the total money Bucky has earned
    total_money_earned = money_earned_sunday + 35  # $35 earned last weekend

    # Calculate the money Bucky still needs to save
    money_left_to_save = 60 - total_money_earned
    result = money_left_to_save
    return result

print(solution())