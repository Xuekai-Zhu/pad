def solution():
    candy_p = 4  # Candy throws 4 pebbles
    lance_p = 3 * candy_p  # Lance throws 3 times as many pebbles as Candy

    # Calculate the difference in the number of pebbles Candy and Lance throw
    diff_p = lance_p - candy_p
    result = diff_p
    return result

print(solution())