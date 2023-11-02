def solution():
    """A vampire drains three people a week. His best friend is a werewolf who eats five people a week, but only fresh ones, never drained ones. How many weeks will a village of 72 people last them both?"""
    # Define the number of people drained by the vampire and eaten by the werewolf each week
    vampire_people = 3
    werewolf_people = 5

    # Define the total number of people in the village
    total_people = 72

    # Calculate the number of weeks until the village runs out of people
    weeks = total_people / (vampire_people + werewolf_people)

    # Return the result rounded up to the nearest whole number
    result = math.ceil(weeks)
    return result

print(solution())