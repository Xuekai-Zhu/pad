def solution():
    """Elmer has a pond that initially contained 2400 pollywogs, but these pollywogs matured into toads and left the pond at a constant rate of 50 pollywogs per day. In addition, Elmer has a son named Melvin, who loves to catch pollywogs, remove them from the pond, and release them into a nearby stream. For the first 20 days, Melvin caught 10 pollywogs per day and released them into the stream. How many days did it take for all of the pollywogs to disappear from the pond?"""
    initial_pollywogs = 2400
    matured_pollywogs_rate = 50
    melvin_daily_catch = 10
    days_with_melvin = 20
    total_matured_pollywogs = 0
    days = 0

    while initial_pollywogs > 0:
        initial_pollywogs -= matured_pollywogs_rate
        total_matured_pollywogs += matured_pollywogs_rate

        if days <= days_with_melvin:
            initial_pollywogs -= melvin_daily_catch

        days += 1

    result = days
    return result

print(solution())