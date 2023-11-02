def solution():
    damon_bands = ["Gorillaz", "Blur", "The Good, the Bad & the Queen", "Elastica", "DRC Music"]
    bernard_bands = ["New Order", "Joy Division", "Electronic", "Bad Lieutenant"]
    if len(damon_bands) > len(bernard_bands):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())