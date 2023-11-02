def solution():
     total_dogs = 40
     female_dogs = total_dogs * (60/100)
     dogs_that_give_birth = female_dogs * (3/4)
     total_puppies = dogs_that_give_birth * 10
     puppies_donated = 130
     total_puppies_left = total_puppies - puppies_donated
     result = total_puppies_left
     return result

print(solution())