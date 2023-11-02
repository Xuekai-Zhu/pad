def solution():
    french_defence_move = "pawn in front of queen forward two spaces"
    four_move_checkmate_defense = "move the queen and bishop to crowd the king"
    if french_defence_move != "pawn in front of queen forward two spaces":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())