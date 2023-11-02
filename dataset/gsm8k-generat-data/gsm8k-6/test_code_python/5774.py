def solution():
    # Calculate the total fees paid by the families for adopting dogs and cats
    total_dog_fees = 15 * 8  # 8 families adopt dogs and pay a fee of $15 each
    total_cat_fees = 13 * 3  # 3 families adopt cats and pay a fee of $13 each
    total_fees = total_dog_fees + total_cat_fees  # total fees paid for adopting animals

    # Calculate the amount donated by the vet to the shelter
    vet_donation = (1/3) * total_fees
    result = vet_donation
    return result

print(solution())