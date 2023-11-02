def solution():
    # Let x be the original number of jewels owned by the dragon
    # The king stole 3, so the dragon now has x-3 jewels
    # The dragon also took twice as many crown jewels, which is 2 times the number stolen (3) = 6 jewels
    # The total number of jewels the dragon now has is (x-3) + 6 = (x+3)
    # The new jewels are a third of the original amount, so (x+3) = (1/3)*x
    # Solving for x, we get x = 9, which is the original number of jewels owned by the dragon

    result = 9
    return result

print(solution())