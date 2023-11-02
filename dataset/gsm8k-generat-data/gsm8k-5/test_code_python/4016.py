def solution():
    # Let's assume the total number of sheep and pigs counted by Mary is 'x'
    # Then the actual number of sheep will be (x/2) - 7, as Mary double-counted 7 sheep
    # And the actual number of pigs will be (x) + 3, as Mary forgot to count 3 pigs
    # And we know that the actual total number of animals is 60
    # So we can set up the equation: (x/2 - 7) + (x + 3) = 60

    x = ((60 - 3 + 7) * 2) / 3  # Solving for x

    # The actual number of animals will be the sum of the actual number of sheep and pigs
    actual_animals = (x / 2 - 7) + (x + 3)
    result = actual_animals
    return result

print(solution())