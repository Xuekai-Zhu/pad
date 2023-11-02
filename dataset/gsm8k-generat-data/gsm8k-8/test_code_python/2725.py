def solution():
    # Calculate the number of female dogs
    num_female_dogs = 0.6 * 40

    # Calculate the number of female dogs giving birth and the total number of puppies
    num_females_giving_birth = 0.75 * num_female_dogs
    num_puppies = 10 * num_females_giving_birth

    # Calculate the number of puppies remaining after donating to the church
    num_puppies_remaining = num_puppies - 130
    result = num_puppies_remaining
    return result

print(solution())