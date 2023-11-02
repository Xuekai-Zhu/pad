def solution():
    # Calculate how many brothers were born in the first half of the year
    first_half_brothers = 0
    for month in ['January', 'February', 'March', 'April', 'May', 'June']:
        if month == 'March':
            first_half_brothers += 3
        else:
            first_half_brothers += 0

    # Calculate how many brothers were born in the second half of the year
    second_half_brothers = 0
    for month in ['July', 'August', 'September', 'October', 'November', 'December']:
        if month in ['October', 'November']:
            second_half_brothers += 1
        elif month == 'December':
            second_half_brothers += 2
        else:
            second_half_brothers += 0

    # Calculate how many presents Santana needs to buy for the first and second half of the year
    first_half_presents = first_half_brothers * 2
    second_half_presents = second_half_brothers * 2

    # Calculate the difference between the two
    difference = second_half_presents - first_half_presents
    result = difference
    return result

print(solution())