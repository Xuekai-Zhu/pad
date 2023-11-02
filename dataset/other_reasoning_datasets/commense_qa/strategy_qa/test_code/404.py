def solution():
    armageddon_believers = ["Evangelicals", "Jehova's Witnesses"]
    religions_looking_forward = ["Evangelicals", "Jehova's Witnesses"]
    overlap = [religion for religion in armageddon_believers if religion in religions_looking_forward]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())