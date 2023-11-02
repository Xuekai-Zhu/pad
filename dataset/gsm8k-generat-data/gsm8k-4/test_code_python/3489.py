def solution():
    """Enrique has 2 132 contracts that he needs to shred. His paper shredder will only allow him to shred 6 pages at a time. How many times will he shred 6 units of paper until all of the contracts are shredded?"""
    # Define the total number of contracts and the number of pages per contract
    total_contracts = 2132
    pages_per_contract = 6

    # Calculate the total number of pages
    total_pages = total_contracts * pages_per_contract

    # Calculate the number of times he needs to shred 6 pages
    times_shred_six = total_pages // 6

    # return the result
    result = times_shred_six
    return result

print(solution())