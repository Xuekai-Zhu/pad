def solution():
    num_women = 30
    num_men = 20
    num_people = num_women + num_men
    fraction_left = 2/5
    num_left = num_people * fraction_left
    num_left_men = 9

    # Calculate the number of people who stayed at the party
    num_stayed = num_people - num_left

    # Calculate the number of women who stayed at the party
    num_stayed_women = num_women - (fraction_left * num_women)
    num_stayed_men = num_men - num_left_men

    # Calculate the difference between the number of women and men who stayed at the party
    diff = num_stayed_women - num_stayed_men
    result = diff
    return result

print(solution())