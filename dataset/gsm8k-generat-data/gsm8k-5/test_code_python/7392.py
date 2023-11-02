def solution():
    sister_shows = 24  # Gina's sister watches 24 shows per week
    gina_ratio = 3  # Gina chooses 3 times as often as her sister does

    # Calculate the total number of shows watched by both sisters
    total_shows = sister_shows + (sister_shows / gina_ratio)

    # Calculate the total time in minutes for all the shows watched
    total_time = total_shows * 50  # Each show is 50 minutes long

    # Calculate the time in minutes that Gina gets to choose
    gina_time = (sister_shows / gina_ratio) * 50  # Gina chooses 3 times as often as her sister does

    result = gina_time
    return result

print(solution())