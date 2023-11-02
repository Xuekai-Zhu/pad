def solution():
     oranges_initial = 60
     oranges_eaten = 10
     oranges_stolen = (oranges_eaten / 2)
     oranges_returned = 5
     oranges_final = oranges_initial - oranges_eaten + oranges_returned

     result = oranges_final
     return result

print(solution())