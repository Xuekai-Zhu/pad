def solution():
    highest_chess_title = "Grand Master"
    well_known_chess_opening = "French Defense"
    if highest_chess_title == "Grand Master":
        if well_known_chess_opening in many_books:
            result = "yes"
        else:
            result = "no"
    else:
        result = "no"
    return result

print(solution())