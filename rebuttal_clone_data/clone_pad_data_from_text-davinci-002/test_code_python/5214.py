def solution():
     when_six_years_old = 6
     when_ten_years_old = 10
     current_age = 16
     num_of_dogs_when_six = 90
     num_of_cars_when_six = num_of_dogs_when_six / 3
     num_of_cars_when_ten = 210
     num_of_dogs_when_ten = (num_of_cars_when_ten - num_of_cars_when_six) + num_of_dogs_when_six
     num_of_cars_current_age = num_of_cars_when_ten * 2
     num_of_dogs_current_age = num_of_cars_current_age - num_of_cars_when_ten + num_of_dogs_when_ten
 
     return num_of_dogs_current_age

print(solution())