def solution():
    # Calculate the number of female baby bunnies Marlon gave to Rodney
    given_bunnies = (2/5) * 30
    # Calculate the number of female baby bunnies left in Marlon's hutch
    remaining_bunnies = 30 - given_bunnies
    # Calculate the total number of bunnies after giving birth to 2 kittens each
    total_bunnies = remaining_bunnies + (remaining_bunnies * 2)
    result = total_bunnies
    return result

print(solution())