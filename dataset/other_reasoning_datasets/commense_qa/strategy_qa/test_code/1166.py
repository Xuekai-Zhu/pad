def solution():
    abba_num_1_hits = 1
    abba_top_10_hits = 4
    beatles_num_1_hits = 20
    beatles_top_10_hits = 34
    if abba_num_1_hits >= beatles_num_1_hits or abba_top_10_hits >= beatles_top_10_hits:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())