def solution():
     susan_cats = 21
     bob_cats = 3
     cats_given_to_bob = 4
     susan_cats_left = susan_cats - cats_given_to_bob
     difference_in_cats = susan_cats_left - bob_cats
     result = difference_in_cats
     return result

print(solution())