def solution():
    # Calculate the total vet fees for dogs
    dog_vet_fees = 15 * 8  # 8 families adopted dogs

    # Calculate the total vet fees for cats
    cat_vet_fees = 13 * 3  # 3 families adopted cats

    # Calculate the total vet fees collected
    total_vet_fees = dog_vet_fees + cat_vet_fees

    # Calculate the amount donated by the vet to the shelter
    vet_donation = total_vet_fees / 3

    result = vet_donation
    return result

print(solution())