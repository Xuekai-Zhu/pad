def solution():
     trips_Brian = 2
     trips_Chris = trips_Brian / 2
     fish_trip_Brian = 400
     fish_trip_Chris = fish_trip_Brian * 2 / 5
     total_fish = fish_trip_Brian * trips_Brian + fish_trip_Chris * trips_Chris
     return total_fish

print(solution())