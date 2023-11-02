def solution():
     mistakes_per_minute = 3/40
     notes_per_minute = 60
     minutes_played = 8
     average_mistakes = mistakes_per_minute * notes_per_minute * minutes_played
     result = average_mistakes
     return result

print(solution())