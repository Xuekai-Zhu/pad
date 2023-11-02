def solution():
     initial_biscuits = 32
     father_gift = 13
     mother_gift = 15
     brother_ate = 20
     biscuits_left = initial_biscuits + father_gift + mother_gift - brother_ate
     result = biscuits_left
     return result

print(solution())