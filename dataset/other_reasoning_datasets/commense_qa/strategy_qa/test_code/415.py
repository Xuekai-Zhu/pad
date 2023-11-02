def solution():
    king_name = "Manuel I"
    spouse_name = "Maria of Aragon"
    sibling_name = "Catherine of Aragon"
    tudor_family = ["Henry VIII", "Catherine of Aragon"]
    if spouse_name in tudor_family or sibling_name in tudor_family:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())