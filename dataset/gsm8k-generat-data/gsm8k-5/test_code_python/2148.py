def solution():
    reality_show_time = 28  # Each reality show is 28 minutes long
    cartoon_time = 10  # The cartoon is 10 minutes long
    num_reality_shows = 5  # Missy watches 5 reality shows
    total_reality_show_time = reality_show_time * num_reality_shows  # Calculate the total time spent watching reality shows
    total_time = total_reality_show_time + cartoon_time  # Add the time spent watching the cartoon
    result = total_time
    return result

print(solution())