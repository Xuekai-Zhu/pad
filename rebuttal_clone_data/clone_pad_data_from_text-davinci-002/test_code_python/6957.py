def solution():
     dog_age = 10
     human_age = 0
     
     if dog_age == 1:
         human_age = 15
     elif dog_age == 2:
         human_age = 24
     else:
         human_age = 24 + (dog_age - 2) * 5
         
     return human_age

print(solution())