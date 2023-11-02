def solution():
    num_vampires = 0.5 * (num_werewolves / 4)  # half the number of werewolves
    num_werewolves_removed = 8

    # Calculate the total amount earned by Van Helsing from removing vampires and werewolves
    total_earned = (num_vampires * 5) + ((num_werewolves - num_werewolves_removed) * 10)

    # Calculate the percentage of werewolves removed
    percent_werewolves_removed = (num_werewolves_removed / num_werewolves) * 100
    result = percent_werewolves_removed
    return result

print(solution())