def solution():
     sharks = 60
     percent_of_pelicans_that_left = 1/3
     pelicans_in_cove = sharks / (2 - percent_of_pelicans_that_left)
     result = pelicans_in_cove
     return result

print(solution())