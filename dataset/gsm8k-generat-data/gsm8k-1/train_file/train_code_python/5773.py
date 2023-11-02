def solution():
    """An animal shelter is having a pet adoption event where owners can adopt an animal for just the cost of the vet fees. Vet fees for dogs are $15, and vet fees for cats are $13. Eight families adopt dogs and three adopt cats. The vet donates a third of the fees they were paid for the adoption checkups back to the shelter. How many dollars did the vet donate?"""
    dog_fee = 15
    cat_fee = 13
    num_dogs = 8
    num_cats = 3
    total_fee = (dog_fee * num_dogs) + (cat_fee * num_cats)
    vet_donation = total_fee / 3
    result = vet_donation
    return result

print(solution())