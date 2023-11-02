def solution():
    sausage_links = 40
    eaten_links = 12
    remaining_links = sausage_links - eaten_links
    ounces_per_link = 1/16
    total_ounces = remaining_links * ounces_per_link
    result = total_ounces
    return result

print(solution())