def solution():
    # Calculate the number of pencils Ken gave to Nilo
    pencils_to_manny = 10
    pencils_to_nilo = pencils_to_manny + 10
    total_pencils_given = pencils_to_manny + pencils_to_nilo
    pencils_left = 50 - total_pencils_given  # Calculate the pencils Ken kept
    result = pencils_left
    return result

print(solution())