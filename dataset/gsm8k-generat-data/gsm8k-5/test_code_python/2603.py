def solution():
    total_toys = 142  # Total number of toys they have all together
    
    # Let's assume Mandy has 'x' number of toys
    x = 1
    # Then Anna has 3 times as many toys as Mandy
    anna_toys = 3 * x
    # And Amanda has 2 more toys than Anna
    amanda_toys = anna_toys + 2

    # Total toys should be equal to the sum of toys each person has
    while (anna_toys + amanda_toys + x) != total_toys:
        x += 1
        anna_toys = 3 * x
        amanda_toys = anna_toys + 2

    # The number of toys Mandy has is 'x'
    result = x
    return result

print(solution())