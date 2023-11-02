def solution():
    """In a 5-day Fishing competition, Jackson was able to reel a total of 6 fishes per day, Jonah was able to reel 4 fishes per day and George was able to reel 8 fishes per day. How many fishes were they able to catch throughout the competition if they are on the same team?"""
    # Define the number of days of the competition
    days = 5

    # Calculate the total number of fish caught by each person
    jackson_fish = 6 * days
    jonah_fish = 4 * days
    george_fish = 8 * days

    # Calculate the total number of fish caught by the team
    total_fish = jackson_fish + jonah_fish + george_fish

    # return the result
    result = total_fish
    return result

print(solution())