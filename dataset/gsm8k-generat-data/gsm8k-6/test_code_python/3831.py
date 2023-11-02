def solution():
    # Calculate the number of firecrackers Jerry has after confiscation
    remaining_firecrackers = 48 - 12

    # Calculate the number of non-defective firecrackers
    good_firecrackers = remaining_firecrackers - (1/6 * remaining_firecrackers)

    # Calculate the number of firecrackers Jerry set off
    set_off_firecrackers = good_firecrackers / 2

    result = set_off_firecrackers
    return result

print(solution())