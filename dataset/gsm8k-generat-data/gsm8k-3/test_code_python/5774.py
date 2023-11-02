def solution():
    """An animal shelter is having a pet adoption event where owners can adopt an animal for just the cost of the vet fees.
    Vet fees for dogs are $15, and vet fees for cats are $13.
    Eight families adopt dogs and three adopt cats.
    The vet donates a third of the fees they were paid for the adoption checkups back to the shelter.
    How many dollars did the vet donate?"""

    # Define the vet fees for dogs and cats
    DOG_FEE = 15
    CAT_FEE = 13

    # Calculate the total fees paid for dog adoptions
    dog_fees = 8 * DOG_FEE

    # Calculate the total fees paid for cat adoptions
    cat_fees = 3 * CAT_FEE

    # Calculate the total fees paid to the vet
    total_fees = dog_fees + cat_fees

    # Calculate the vet's donation to the shelter
    donation = total_fees / 3

    # Display the vet's donation
    result = donation
    return result

print(solution())