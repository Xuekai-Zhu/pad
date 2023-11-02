def solution():
    cyrus_bites = 14 + 10
    fam_bites = cyrus_bites / 2
    num_family_members = 6
    total_bites = cyrus_bites + fam_bites
    bites_per_member = total_bites / (num_family_members + 1)  # add 1 to include Cyrus
    result = bites_per_member
    return result

print(solution())