def solution():
    # Calculate the total number of pages in the contracts
    total_pages = 2132 * 6  # each contract has 6 pages

    # Calculate the number of times Enrique needs to shred 6 pages to shred all the contracts
    shred_times = total_pages // 6  # integer division to find the number of times
    result = shred_times
    return result

print(solution())