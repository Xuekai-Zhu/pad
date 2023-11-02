def solution():
    famous_painters = ["Jackson Pollock"]
    straight_edge_artists = []
    for artist in famous_painters:
        if artist == "Jackson Pollock":
            alcoholism = True
            break
    if alcoholism:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())