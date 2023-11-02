def solution():
    # Calculate the total number of pairs of socks Lisa ended up with
    lisa_start = 12
    sandra = 20
    cousin = sandra/5
    mom = 8 + 3*lisa_start
    total_socks = lisa_start + sandra + cousin + mom
    result = total_socks
    return result

print(solution())