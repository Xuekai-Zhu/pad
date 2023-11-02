def solution():
     vet_fee_dogs = 15
     vet_fee_cats = 13
     adopted_dogs = 8
     adopted_cats = 3
     vet_fee_total = (vet_fee_dogs * adopted_dogs) + (vet_fee_cats * adopted_cats)
     donation = (vet_fee_total / 3)
     result = donation
     return result

print(solution())