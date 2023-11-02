def solution():
    # Calculate the total length of the movie and advertisement
    movie_length = 1.5 + 0.33  # 1.5 hours for the movie and 20 minutes or 0.33 hours for the advertisement

    # Calculate the total operating hours of the movie theater each day
    total_hours = movie_length * 6  # 6 replays per day
    result = total_hours
    return result

print(solution())