def solution():
    # Calculate the number of swans at Rita's pond in 10 years
    num_swans = 15 * (2 ** 5)  # the number of swans doubles every 2 years, so after 10 years it will be 2^5 times the current amount
    result = num_swans
    return result

print(solution())