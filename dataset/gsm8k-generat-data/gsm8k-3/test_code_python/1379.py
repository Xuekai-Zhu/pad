def solution():
    """Lola’s rabbits keep having kittens each spring. During the first spring, her 10 breeding rabbits had 10 times as many kittens as the number of breeding rabbits Lola has, and half of the kittens got adopted. 5 of them had to be returned to Lola due to re-homing problems. During the next spring, her 10 breeding rabbits only had a total of 60 kittens, with 4 of the kittens being adopted. Including the breeding rabbits, how many rabbits does Lola have in her house?"""
    # Define the number of breeding rabbits Lola started with
    breeding_rabbits = 10

    # Calculate the number of kittens in the first spring
    kitten_ratio = 10
    kittens_1 = breeding_rabbits * kitten_ratio
    adopted_1 = kittens_1 / 2
    returned_1 = 5
    kittens_1 -= adopted_1
    kittens_1 += returned_1

    # Calculate the number of rabbits after the first spring
    rabbits_1 = breeding_rabbits + kittens_1

    # Calculate the number of kittens in the second spring
    kittens_2 = 60 - breeding_rabbits
    adopted_2 = 4
    kittens_2 -= adopted_2

    # Calculate the total number of rabbits
    rabbits_total = rabbits_1 + kittens_2

    # Display the total number of rabbits
    result = rabbits_total
    return result

print(solution())