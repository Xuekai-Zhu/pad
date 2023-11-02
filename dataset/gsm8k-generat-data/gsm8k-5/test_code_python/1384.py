def solution():
    pots_per_shelf = 5*3  # Bill can stack 5 pots vertically and 3 sets of vertically stacked pots side-by-side on each shelf
    total_pots = 60  # Bill needs to stack 60 pots in total

    # Calculate the total number of shelves needed
    shelves_needed = total_pots / pots_per_shelf

    # Round up to the nearest whole number since Bill can't have a partial shelf
    shelves_needed = math.ceil(shelves_needed)
    result = shelves_needed
    return result

print(solution())