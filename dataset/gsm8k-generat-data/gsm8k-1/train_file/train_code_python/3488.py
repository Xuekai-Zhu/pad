def solution():
    """Enrique has 2 132 contracts that he needs to shred. His paper shredder will only allow him to shred 6 pages at a time. How many times will he shred 6 units of paper until all of the contracts are shredded?"""
    total_contracts = 2132
    pages_per_shred = 6
    total_shreds = total_contracts * pages_per_contract / pages_per_shred
    result = total_shreds
    return result

print(solution())