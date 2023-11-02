def solution():
    """Van Helsing gets paid by the town to remove all the vampires and werewolves. He gets $5 per vampire and $10 per werewolf. He removes half the vampires and removes 8 werewolves, and earned $105. There were 4 times as many werewolves as vampires. What percentage of the werewolves did he remove?"""
    # Define the price per vampire and werewolf
    VAMPIRE_PRICE = 5
    WEREWOLF_PRICE = 10

    # Define the number of vampires and werewolves
    vampires = None
    werewolves = None

    # Define the total earnings
    total_earnings = 105

    # Define the ratio of werewolves to vampires
    werewolf_vampire_ratio = 4

    # Define the number of werewolves removed
    werewolves_removed = 8

    # Calculate the number of werewolves and vampires based on the given ratios and information
    vampires = (werewolves_removed * werewolf_vampire_ratio) / 2
    werewolves = werewolves_removed * werewolf_vampire_ratio

    # Calculate the total earnings from removing the vampires and werewolves
    total_earnings_calculated = (vampires * VAMPIRE_PRICE) + (werewolves * WEREWOLF_PRICE)

    # Calculate the percentage of werewolves removed
    werewolves_percentage_removed = (werewolves_removed / werewolves) * 100

    # Return the result
    result = werewolves_percentage_removed
    return result

print(solution())