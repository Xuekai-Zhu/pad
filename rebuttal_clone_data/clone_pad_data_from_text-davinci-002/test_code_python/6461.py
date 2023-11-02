def solution():
     initial_amount = 200
     amount_given_to_mother = initial_amount * (3/8)
     amount_given_to_father = initial_amount * (3/10)
     amount_left = initial_amount - (amount_given_to_mother + amount_given_to_father)
     result = amount_left
     return result

print(solution())