def solution():
    """Van Helsing gets paid by the town to remove all the vampires and werewolves. He gets $5 per vampire and $10 per werewolf. He removes half the vampires and removes 8 werewolves, and earned $105. There were 4 times as many werewolves as vampires. What percentage of the werewolves did he remove?"""
    # Define the payment per vampire and per werewolf
    VAMPIRE_PAYMENT = 5
    WEREWOLF_PAYMENT = 10

    # Define the total payment received by Van Helsing
    total_payment = 105

    # Determine the number of werewolves removed
    werewolves_removed = 8

    # Determine the number of vampires and werewolves
    # Let x be the number of vampires
    # Then there are 4x werewolves
    x = (2 * total_payment - werewolves_removed * WEREWOLF_PAYMENT) / (2 * VAMPIRE_PAYMENT + WEREWOLF_PAYMENT)
    vampires = x
    werewolves = 4 * x

    # Determine the number of werewolves removed as a percentage of the total number of werewolves
    werewolf_percentage_removed = werewolves_removed / werewolves * 100

    # Display the percentage of werewolves removed
    result = werewolf_percentage_removed
    return result

print(solution())