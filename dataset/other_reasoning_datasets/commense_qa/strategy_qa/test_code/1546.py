def solution():
    john_kerry_alma_mater = "Yale University"
    golden_globe_winners = {"Jennifer Connelly": "Yale University"}
    for winner, alma_mater in golden_globe_winners.items():
        if alma_mater == john_kerry_alma_mater:
            result = "yes"
            break
    else:
        result = "no"
    return result

print(solution())