def solution():
    """Aren’s flight from New York to Hawaii will take 11 hours 20 minutes. He spends 2 hours reading, 4 hours watching two movies, 30 minutes eating his dinner, 40 minutes listening to the radio, and 1 hour 10 minutes playing games. How many hours does he have left to take a nap?"""
    total_flight_time = 11 * 60 + 20 # in minutes
    read_time = 2 * 60 # in minutes
    movie_time = 4 * 60 # in minutes
    dinner_time = 30 # in minutes
    radio_time = 40 # in minutes
    game_time = 1 * 60 + 10 # in minutes

    total_time_spent = read_time + movie_time + dinner_time + radio_time + game_time
    remaining_time = total_flight_time - (total_time_spent / 60) # in hours
    result = remaining_time
    
    return result

print(solution())