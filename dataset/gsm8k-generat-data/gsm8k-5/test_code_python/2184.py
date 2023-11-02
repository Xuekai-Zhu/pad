def solution():
    # Let x be the number of cats Frankie has
    # Then he has x+6 snakes and x-1 parrots
    # He has a total of x + (x+6) + (x-1) + 2 (dogs) = 3x + 7 pets
    # Six of his pets (assuming they are not dogs) have 4 legs, so he has 3x+1=6 pets with 4 legs
    # Solving for x, we get x=1, so Frankie has 1+7=8 pets in total
    result = 8
    return result

print(solution())