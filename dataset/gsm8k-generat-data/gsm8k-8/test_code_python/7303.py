def solution():
    total_rice = 50
    storage_rice = total_rice * (7/10)
    given_rice = total_rice - storage_rice
    difference = storage_rice - given_rice
    result = difference
    return result

print(solution())