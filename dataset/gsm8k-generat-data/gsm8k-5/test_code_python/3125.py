def solution():
    # Let's assume there were 'v' vampires and 'w' werewolves originally
    # We know that 'w' = 4*v (as there were 4 times as many werewolves as vampires)

    w = 4
    v = 1

    # Initially, Van Helsing removes half the vampires, which means he removes v/2 vampires
    # He also removes 8 werewolves
    # So, his earnings would be 5*(v/2) + 10*(w-8)

    while 5 * (v / 2) + 10 * (w - 8) != 105:
        if w > 8:
            w -= 1
            v = w // 4
        else:
            w = 4 * (v + 1)

    # Now we know that w=16 and v=4, so Van Helsing made $50 + $90 = $140
    # To find the percentage of werewolves he removed, we need to know the total number of werewolves he started with
    total_werewolves = w + 8  # He removed 8 werewolves, but we don't know how many there were to begin with

    percentage_removed = (8 / total_werewolves) * 100
    result = percentage_removed
    return result

print(solution())