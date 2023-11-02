def solution():
     hours_on_train = 9
     hours_reading = 2
     hours_eating = 1
     hours_watching_movies = 3
     hours_left = hours_on_train - (hours_reading + hours_eating + hours_watching_movies)
     result = hours_left
     return result

print(solution())