def solution():
    # Define the cost of vet fees for each animal
    dog_fee = 15
    cat_fee = 13

    # Calculate the total vet fee income for the shelter
    total_dog_fees = 8 * dog_fee
    total_cat_fees = 3 * cat_fee
    total_vet_fees = total_dog_fees + total_cat_fees

    # Calculate the amount the vet donates back to the shelter
    vet_donation = total_vet_fees / 3
    result = vet_donation
    return result

print(solution())