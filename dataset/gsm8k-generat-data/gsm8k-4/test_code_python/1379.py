def solution():
    """Lola’s rabbits keep having kittens each spring. During the first spring, her 10 breeding rabbits had 10 times as many kittens as the number of breeding rabbits Lola has, and half of the kittens got adopted. 5 of them had to be returned to Lola due to re-homing problems. During the next spring, her 10 breeding rabbits only had a total of 60 kittens, with 4 of the kittens being adopted. Including the breeding rabbits, how many rabbits does Lola have in her house?"""
    # Define the number of breeding rabbits in the first spring
    breeding_rabbits_spring1 = 10

    # Calculate the number of kittens in the first spring
    kittens_spring1 = breeding_rabbits_spring1 * 10

    # Calculate the number of adopted kittens in the first spring
    adopted_spring1 = kittens_spring1 / 2

    # Calculate the number of returned kittens in the first spring
    returned_spring1 = 5

    # Calculate the number of kittens remaining with Lola after the first spring
    remaining_spring1 = kittens_spring1 - adopted_spring1 + returned_spring1

    # Calculate the number of breeding rabbits needed in the next spring to produce 60 kittens
    breeding_rabbits_spring2 = 60 / remaining_spring1

    # Calculate the total number of kittens in the next spring
    kittens_spring2 = breeding_rabbits_spring2 * 10

    # Calculate the number of adopted kittens in the next spring
    adopted_spring2 = 4

    # Calculate the total number of rabbits including breeding rabbits
    total_rabbits = breeding_rabbits_spring1 + breeding_rabbits_spring2 + remaining_spring1 + kittens_spring2 - adopted_spring2

    result = total_rabbits
    return result

print(solution())