def solution():
    van_goh_valuable_artwork = True
    van_goh_print_readily_available = True
    if van_goh_valuable_artwork and not van_goh_print_readily_available:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())