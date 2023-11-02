def solution():
    dog_vet_fee = 15
    cat_vet_fee = 13
    num_dogs = 8
    num_cats = 3

    # Calculate the total vet fees collected for dogs
    total_dog_fees = num_dogs * dog_vet_fee

    # Calculate the total vet fees collected for cats
    total_cat_fees = num_cats * cat_vet_fee

    # Calculate the total vet fees collected
    total_fees = total_dog_fees + total_cat_fees

    # Calculate the amount donated by the vet
    donation_amount = total_fees / 3

    result = donation_amount
    return result

print(solution())