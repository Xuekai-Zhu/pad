def solution():
    # Calculate the total number of items in the store before any sales
    starting_total = 4458 + 575

    # Calculate the total number of items sold
    sold_total = 1561

    # Calculate the remaining number of items in the store
    remaining_total = starting_total - sold_total

    result = remaining_total
    return result

print(solution())