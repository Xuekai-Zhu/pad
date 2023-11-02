def solution():
    # Calculate the total number of beats played by John in 3 days
    beats_per_hour = 200 * 60  # John can play 200 beats per minute which equals 12,000 beats per hour
    total_beats = beats_per_hour * 2 * 3  # John plays for 2 hours a day for 3 days
    result = total_beats
    return result

print(solution())