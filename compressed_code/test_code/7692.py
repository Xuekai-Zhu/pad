def solution():
    
    songs_per_day_vivian = 10
    songs_per_day_clara = songs_per_day_vivian - 2
    days_in_june = 30
    weekend_days_in_june = 8
    total_days_june = days_in_june - weekend_days_in_june
    total_songs_vivian = songs_per_day_vivian * total_days_june
    total_songs_clara = songs_per_day_clara * total_days_june
    total_songs_both = total_songs_vivian + total_songs_clara
    result = total_songs_both
    return result

print(solution())