def solution():
    """Elmer has a pond that initially contained 2400 pollywogs, but these pollywogs matured into toads and left the pond at a constant rate of 50 pollywogs per day. In addition, Elmer has a son named Melvin, who loves to catch pollywogs, remove them from the pond, and release them into a nearby stream. For the first 20 days, Melvin caught 10 pollywogs per day and released them into the stream. How many days did it take for all of the pollywogs to disappear from the pond?"""
    initial_pollywogs = 2400
    matured_pollywogs_per_day = 50
    melvin_catches_per_day = 10
    days_until_maturity = initial_pollywogs // matured_pollywogs_per_day
    remaining_pollywogs = initial_pollywogs - days_until_maturity*matured_pollywogs_per_day
    for i in range(1, 21):
        remaining_pollywogs -= melvin_catches_per_day
    days_until_disappearance = days_until_maturity + (remaining_pollywogs // matured_pollywogs_per_day)
    result = days_until_disappearance
    return result

print(solution())