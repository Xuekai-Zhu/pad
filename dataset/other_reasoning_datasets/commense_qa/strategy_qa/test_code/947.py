def solution():
    snowdon_peak_height = 3560
    everest_peak_height = 29029
    if snowdon_peak_height < everest_peak_height:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())