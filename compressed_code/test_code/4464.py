def solution():
    
    dog_fee = 15
    cat_fee = 13
    num_dogs = 8
    num_cats = 3
    total_fees = (dog_fee * num_dogs) + (cat_fee * num_cats)
    vet_donation = total_fees * (1 / 3)
    result = vet_donation
    return result

print(solution())