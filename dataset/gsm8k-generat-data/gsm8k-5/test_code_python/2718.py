def solution():
    trumpets_weight = 5 * 6  # 6 trumpets carry 5 pounds each
    clarinets_weight = 5 * 9  # 9 clarinets carry 5 pounds each
    trombones_weight = 10 * 8  # 8 trombones carry 10 pounds each
    tubas_weight = 20 * 3  # 3 tubas carry 20 pounds each
    drummers_weight = 15 * 2  # 2 drummers carry 15 pounds each

    # Calculate the total weight carried by the marching band
    total_weight = trumpets_weight + clarinets_weight + trombones_weight + tubas_weight + drummers_weight
    result = total_weight
    return result

print(solution())