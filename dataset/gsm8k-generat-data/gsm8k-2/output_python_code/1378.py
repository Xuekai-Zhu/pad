def solution():
    """Lola’s rabbits keep having kittens each spring. During the first spring, her 10 breeding rabbits had 10 times as many kittens as the number of breeding rabbits Lola has, and half of the kittens got adopted. 5 of them had to be returned to Lola due to re-homing problems. During the next spring, her 10 breeding rabbits only had a total of 60 kittens, with 4 of the kittens being adopted. Including the breeding rabbits, how many rabbits does Lola have in her house?"""
    breeding_rabbits_first = 10
    kittens_first = breeding_rabbits_first * 10
    adopted_first = kittens_first / 2
    returned_first = 5
    remaining_first = kittens_first / 2 - returned_first
    breeding_rabbits_second = 10
    kittens_second = 60
    adopted_second = 4
    remaining_second = kittens_second - adopted_second
    total_rabbits = breeding_rabbits_first + remaining_first + breeding_rabbits_second + remaining_second
    result = total_rabbits
    return result

print(solution())