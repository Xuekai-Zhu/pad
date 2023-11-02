def solution():
    """Van Helsing gets paid by the town to remove all the vampires and werewolves. He gets $5 per vampire and $10 per werewolf. He removes half the vampires and removes 8 werewolves, and earned $105. There were 4 times as many werewolves as vampires. What percentage of the werewolves did he remove?"""
    vampires = None
    werewolves = None

    # Find the number of vampires and werewolves
    for i in range(1, 101):
        for j in range(1, 101):
            if i + j == 2 * (i/2) + 8 and j == 4*i:
                vampires = i
                werewolves = j
                break
        if vampires and werewolves:
            break

    # Calculate the total amount earned
    total_earned = 5 * (vampires/2) + 10 * (werewolves - 8)

    # Calculate the percentage of werewolves removed
    removed_werewolves = werewolves - 8
    percentage_removed = (removed_werewolves / werewolves) * 100

    result = percentage_removed
    return result

print(solution())