def solution():
    political_association = "triumvirate"
    reality_shows = ["The Challenge: Total Madness", "American Idol"]
    reality_shows_with_triumvirates = [show for show in reality_shows if political_association in show]
    if reality_shows_with_triumvirates:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())