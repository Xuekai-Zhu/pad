def solution():
    # Calculate the total number of pens Kendra has
    kendra_pens = 4 * 3

    # Calculate the total number of pens Tony has
    tony_pens = 2 * 3

    # Calculate the total number of pens they have
    total_pens = kendra_pens + tony_pens

    # Keep two pens each
    total_pens -= 4

    # Calculate the number of friends they can give pens to
    friends = total_pens // 1
    result = friends
    return result

print(solution())