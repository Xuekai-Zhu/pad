def solution():
     individuals_that_like_football = 24
     individuals_that_play_football = 12
     percentage_of_people_that_like_football = 50
     people_that_play_football = individuals_that_like_football * percentage_of_people_that_like_football / 100
     total_people = 250
     result = people_that_play_football * total_people / individuals_that_like_football
     
     return result

print(solution())