def solution():
    """A vampire drains three people a week. His best friend is a werewolf who eats five people a week, but only fresh ones, never drained ones. How many weeks will a village of 72 people last them both?"""
    # Define the number of people the vampire and werewolf drain/eat per week
    vampire_people_per_week = 3
    werewolf_people_per_week = 5

    # Define the total number of people in the village
    total_people = 72

    # Calculate the number of weeks the vampire and werewolf can survive
    weeks_survived = total_people / (vampire_people_per_week + werewolf_people_per_week)

    # Display the number of weeks they can survive
    result = weeks_survived
    return result

print(solution())