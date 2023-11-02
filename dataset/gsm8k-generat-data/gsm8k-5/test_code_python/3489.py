def solution():
    contracts = 2 * 132  # Enrique has a total of 264 contracts to shred
    pages_per_contract = 6  # He can shred 6 pages at a time
    total_pages = contracts * pages_per_contract  # Calculate the total number of pages to shred

    # Calculate the number of times he needs to shred 6 pages to shred all the contracts
    shredding_times = total_pages // 6
    result = shredding_times
    return result

print(solution())