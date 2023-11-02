def solution():
    # Calculate the melting rate of each individual popsicle
    melting_rate = []
    for i in range(6):
        melting_rate.append(2 ** i)

    # Calculate the ratio of the melting rate of the last popsicle to the first popsicle
    ratio = melting_rate[-1] / melting_rate[0]
    result = ratio
    return result

print(solution())