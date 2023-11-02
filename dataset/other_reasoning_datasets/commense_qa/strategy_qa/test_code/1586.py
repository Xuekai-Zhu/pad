def solution():
    walt_disney_awards = 26
    six_flags_founder_awards = 0
    knotts_berry_founder_awards = 0
    if walt_disney_awards > six_flags_founder_awards and walt_disney_awards > knotts_berry_founder_awards:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())