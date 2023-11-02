def solution():
    lisa_pairs = 12
    sandra_pairs = 20
    cousin_pairs = sandra_pairs / 5
    mom_pairs = (lisa_pairs * 3) + 8

    total_pairs = lisa_pairs + sandra_pairs + cousin_pairs + mom_pairs
    result = total_pairs
    return result

print(solution())