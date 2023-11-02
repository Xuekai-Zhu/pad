def solution():
    """Sam shared a sum of money between his three cousins Sandra, Amy and Ruth in the ratio 2:1:3 respectively. If Amy got $50, how much did Sandra get?"""
    # Define the ratio of the amounts received by Sandra, Amy, and Ruth
    ratio = [2, 1, 3]

    # Get the total number of parts in the ratio
    total_ratio = sum(ratio)

    # Get the fraction of the sum of money that Amy received
    amy_fraction = ratio[1] / total_ratio

    # Calculate the total sum of money shared
    total_money = 50 / amy_fraction

    # Calculate the amount that Sandra received
    sandra_amount = total_money * (ratio[0] / total_ratio)

    # Display the amount that Sandra received
    result = sandra_amount
    return result

print(solution())