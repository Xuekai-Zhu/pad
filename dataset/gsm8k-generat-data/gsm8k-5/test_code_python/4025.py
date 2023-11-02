def solution():
    vampire_rate = 3  # The vampire drains 3 people per week
    werewolf_rate = 5  # The werewolf eats 5 people per week, but only fresh ones

    total_people = 72  # The village has 72 people

    # Calculate how many weeks the vampire and werewolf can survive with the given number of people
    weeks = total_people / (vampire_rate + werewolf_rate)
    result = weeks
    return result

print(solution())