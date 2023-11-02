def solution():
    dozens_bought = 3  # Emma bought 3 dozens of macarons
    additional_pieces = 10  # Emma also bought 10 individual pieces of macarons
    total_pieces = dozens_bought * 12 + additional_pieces  # Emma had a total of 46 pieces of macarons
    left_over = 15  # There were 15 pieces of macarons left over
    eaten_pieces = total_pieces - left_over  # Calculate how many pieces were eaten

    result = eaten_pieces
    return result

print(solution())