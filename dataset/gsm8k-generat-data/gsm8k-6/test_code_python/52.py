def solution():
    # Calculate the total number of pencils
    total_pencils = 5 * 8 + 10  # Arnel shared the remaining pencils equally with his 5 friends, and kept 10 pencils

    # Calculate the number of pencils in each box
    pencils_per_box = total_pencils / 10  # Arnel had 10 boxes of pencils with the same number of pencils in each box

    result = pencils_per_box
    return result

print(solution())