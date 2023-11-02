def solution():
    """Anthony had 50 pencils. He gave 1/2 of his pencils to Brandon, and he gave 3/5 of the remaining pencils to Charlie. He kept the remaining pencils. How many pencils did Anthony keep?"""
    total_pencils = 50
    pencils_given_to_brandon = total_pencils / 2
    pencils_remaining = total_pencils - pencils_given_to_brandon
    pencils_given_to_charlie = pencils_remaining * (3/5)
    pencils_kept = pencils_remaining - pencils_given_to_charlie
    result = pencils_kept
    return result

print(solution())