def solution():
    """Lola’s rabbits keep having kittens each spring. During the first spring, her 10 breeding rabbits had 10 times as many kittens as the number of breeding rabbits Lola has, and half of the kittens got adopted. 5 of them had to be returned to Lola due to re-homing problems. During the next spring, her 10 breeding rabbits only had a total of 60 kittens, with 4 of the kittens being adopted. Including the breeding rabbits, how many rabbits does Lola have in her house?"""
    
    # First spring
    breeding_rabbits = 10
    first_spring_kittens = breeding_rabbits * 10
    adopted_kittens = first_spring_kittens / 2
    returned_kittens = 5
    remaining_kittens = first_spring_kittens - adopted_kittens + returned_kittens
    
    # Second spring
    total_kittens = remaining_kittens + 60
    adopted_kittens = 4
    remaining_rabbits = breeding_rabbits + (total_kittens // 10)
    total_rabbits = remaining_rabbits + adopted_kittens
    
    result = total_rabbits
    return result

print(solution())