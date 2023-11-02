def solution():
    
    initial_socks = 40
    lost_socks = 4
    remaining_socks = initial_socks - lost_socks
    donated_socks = remaining_socks * (2/3)
    remaining_socks -= donated_socks
    purchased_socks = 10
    gifted_socks = 3
    total_socks = remaining_socks + purchased_socks + gifted_socks
    result = total_socks
    return result

print(solution())