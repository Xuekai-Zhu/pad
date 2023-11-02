def solution():
    # Calculate the number of boys and girls who brought gifts
    boys_with_gifts = 0.75 * 16
    girls_with_gifts = 6/7 * 14

    # Calculate the total number of people who brought gifts
    total_with_gifts = boys_with_gifts + girls_with_gifts

    # Calculate the total number of people who attended the party
    total_attended = 16 + 14

    # Calculate the number of people who did not bring gifts
    no_gifts = total_attended - total_with_gifts
    result = no_gifts
    return result

print(solution())