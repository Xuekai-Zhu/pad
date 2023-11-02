def solution():
    # Calculate the number of boys and girls who brought gifts
    boys_with_gifts = (3/4) * 16
    girls_with_gifts = (6/7) * 14

    # Calculate the total number of people who brought gifts
    total_with_gifts = boys_with_gifts + girls_with_gifts

    # Calculate the number of people who did not bring gifts
    total_attended = 16 + 14
    no_gifts = total_attended - total_with_gifts

    result = no_gifts
    return result

print(solution())