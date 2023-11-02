def solution():
    farthings = 54
    pfennigs = 2
    farthings_per_pfennig = 6
    pfennigs_after_transaction = farthings - (pfennigs * farthings_per_pfennig)
    result = pfennigs_after_transaction
    return result

print(solution())