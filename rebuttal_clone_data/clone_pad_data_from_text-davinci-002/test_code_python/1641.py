def solution():
     minutes_between_uses = 50
     movie_length_in_hours = 2.5
     movie_length_in_minutes = movie_length_in_hours * 60
     number_of_uses = movie_length_in_minutes / minutes_between_uses
     result = number_of_uses
     return result

print(solution())