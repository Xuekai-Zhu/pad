def solution():
    # Calculate the amount of scholarship received by Kelly and Nina
    wendy_scholarship = 20000
    kelly_scholarship = 2 * wendy_scholarship
    nina_scholarship = kelly_scholarship - 8000

    # Calculate the total amount of scholarship received
    total_scholarship = wendy_scholarship + kelly_scholarship + nina_scholarship
    result = total_scholarship
    return result

print(solution())