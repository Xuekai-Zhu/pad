def solution():
    # Define the variables
    vampire_payment = 5
    werewolf_payment = 10

    # Calculate the number of vampires and werewolves
    x = 2  # assume there are 2 vampires (removed half of the total)
    y = 8  # given that he removed 8 werewolves
    werewolf_to_vampire_ratio = 4  # given that there are 4 times as many werewolves as vampires
    total_werewolves = werewolf_to_vampire_ratio * x

    # Calculate the total payment received
    total_payment = (x * vampire_payment) + (y * werewolf_payment)

    # Calculate the remaining werewolves
    remaining_werewolves = total_werewolves - y

    # Calculate the percentage of removed werewolves
    removed_werewolves_percentage = (y / total_werewolves) * 100

    result = removed_werewolves_percentage
    return result

print(solution())