def solution():
    ryans_party = 4
    taylors_party = 1
    combined_party = 240
    ryans_party_size = combined_party / (1 + (1/ryans_party))
    result = ryans_party_size
    return result

print(solution())