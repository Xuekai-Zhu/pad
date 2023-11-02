def solution():
    """In a 5-day Fishing competition, Jackson was able to reel a total of 6 fishes per day, Jonah was able to reel 4 fishes per day and George was able to reel 8 fishes per day. How many fishes were they able to catch throughout the competition if they are on the same team?"""
    # Define the number of days in the competition
    DAYS = 5

    # Define the number of fish each person can catch per day
    JACKSON = 6
    JONAH = 4
    GEORGE = 8

    # Calculate the total number of fish caught by each person
    jackson_total = JACKSON * DAYS
    jonah_total = JONAH * DAYS
    george_total = GEORGE * DAYS

    # Calculate the total number of fish caught by the team
    team_total = jackson_total + jonah_total + george_total

    # Display the total number of fish caught by the team
    result = team_total
    return result

print(solution())