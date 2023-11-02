def solution():
    # Calculate the total number of dog nails
    dog_nails_per_foot = 4
    dog_feet_per_dog = 4
    total_dog_nails = dog_nails_per_foot * dog_feet_per_dog * 4

    # Calculate the total number of parrot nails
    parrot_claws_per_leg = 3
    parrot_legs_per_parrot = 2
    total_normal_parrot_claws = parrot_claws_per_leg * parrot_legs_per_parrot * 8
    total_special_parrot_claws = parrot_claws_per_leg * 1
    total_parrot_nails = total_normal_parrot_claws + total_special_parrot_claws

    # Calculate the total number of nails Cassie needs to cut
    total_nails_to_cut = total_dog_nails + total_parrot_nails
    result = total_nails_to_cut
    return result

print(solution())