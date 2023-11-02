def solution():
    num_prophets = 124000
    num_solomon = 25
    num_kings = 20
    perc_prophets_with_solomon = (num_solomon / num_prophets) * 100
    perc_kings_with_solomon = (num_solomon / num_kings) * 100
    if perc_prophets_with_solomon > perc_kings_with_solomon:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())