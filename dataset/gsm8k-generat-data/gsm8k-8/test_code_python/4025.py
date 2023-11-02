def solution():
    # Define the number of people the vampire and werewolf drain/eat per week
    vampire_drains = 3
    werewolf_eats = 5

    # Calculate the total number of people they consume per week
    total_consumption = vampire_drains + werewolf_eats

    # Calculate the number of weeks the village of 72 people will last them both
    weeks_lasted = 72 / total_consumption
    result = weeks_lasted
    return result

print(solution())