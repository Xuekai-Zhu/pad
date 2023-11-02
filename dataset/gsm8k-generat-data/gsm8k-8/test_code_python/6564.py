def solution():
    # Calculate the number of women who support the idea
    women_support = 0.35 * 0.5 * poll_size

    # Calculate the number of women who oppose the idea
    women_oppose = 0.5 * poll_size - women_support

    # Calculate the total number of people who oppose the idea
    total_oppose = women_oppose + 39

    # Calculate the total number of people in the poll
    poll_size = total_oppose / (1 - 0.35)

    result = poll_size
    return result

print(solution())