def solution():
    bill_nye_birth_year = 1955
    fdr_last_election_year = 1944
    if bill_nye_birth_year > fdr_last_election_year:
        result = "no"
    else:
        result = "unable to determine"
    return result

print(solution())