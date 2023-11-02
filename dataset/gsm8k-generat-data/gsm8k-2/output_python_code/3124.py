def solution():
    """Van Helsing gets paid by the town to remove all the vampires and werewolves. He gets $5 per vampire and $10 per werewolf. He removes half the vampires and removes 8 werewolves, and earned $105. There were 4 times as many werewolves as vampires. What percentage of the werewolves did he remove?"""
    total_earnings = 105
    vampire_pay = 5
    werewolf_pay = 10
    removed_werewolves = 8

    # Let's assume "x" as the number of werewolves
    x = 4
    vampires = x / 4

    # Van Helsing removes half the vampires
    removed_vampires = vampires / 2

    # Calculate the total earnings
    earnings = (removed_vampires * vampire_pay) + ((x - removed_werewolves) * werewolf_pay)

    # Find the percentage of removed werewolves
    removed_percentage = (removed_werewolves / x) * 100

    result = removed_percentage
    return result

print(solution())