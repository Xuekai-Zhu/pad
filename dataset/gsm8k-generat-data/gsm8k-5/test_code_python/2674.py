def solution():
    # Daisy starts with 5 dog toys on Monday
    num_toys = 5

    # Daisy has 3 toys left after Tuesday and her owner buys her 3 more, bringing the total to 6
    num_toys += 3
    num_toys += 3

    # Daisy's owner buys her 5 more toys on Wednesday, bringing the total to 11
    num_toys += 5

    result = num_toys
    return result

print(solution())