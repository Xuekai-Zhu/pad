def solution():
    """An animal shelter is having a pet adoption event where owners can adopt an animal for just the cost of the vet fees. Vet fees for dogs are $15, and vet fees for cats are $13. Eight families adopt dogs and three adopt cats. The vet donates a third of the fees they were paid for the adoption checkups back to the shelter. How many dollars did the vet donate?"""
    # Define the vet fees for dogs and cats
    dog_fee = 15
    cat_fee = 13

    # Calculate the total amount paid for dog adoptions
    dog_adoption_total = 8 * dog_fee

    # Calculate the total amount paid for cat adoptions
    cat_adoption_total = 3 * cat_fee

    # Calculate the total amount paid for all adoptions
    total_adoption_fees = dog_adoption_total + cat_adoption_total

    # Calculate the amount donated by the vet
    vet_donation = total_adoption_fees / 3

    # return the result
    result = vet_donation
    return result

print(solution())