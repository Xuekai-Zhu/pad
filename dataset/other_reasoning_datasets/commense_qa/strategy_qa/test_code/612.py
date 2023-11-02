def solution():
    possible_sources = ["mythology"]
    june_sources = ["Juno"]
    overlap = [source for source in possible_sources if source in june_sources]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())