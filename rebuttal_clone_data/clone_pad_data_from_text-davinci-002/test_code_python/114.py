def solution():
     """Ed has 2 dogs, 3 cats and twice as many fish as cats and dogs combined. How many pets does Ed have in total?"""
     dogs = 2
     cats = 3
     fish = (dogs + cats) * 2
     total_pets = dogs + cats + fish
     result = total_pets
     return result

print(solution())