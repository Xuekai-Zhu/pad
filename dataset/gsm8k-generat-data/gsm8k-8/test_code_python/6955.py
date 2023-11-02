def solution():
    # Calculate the length of practice on Thursday
    thurs_practice = 50

    # Calculate the length of practice on Wednesday
    wed_practice = thurs_practice + 5

    # Calculate the length of practice on Tuesday
    tues_practice = wed_practice - 10

    # Calculate the length of practice on Monday
    mon_practice = 2 * tues_practice

    # Calculate the total practice time so far
    total_practice = mon_practice + tues_practice + wed_practice + thurs_practice

    # Calculate how much more practice Carlo needs to do
    remaining_practice = (5 * 60) - total_practice

    # Calculate how much Carlo should practice on Friday
    fri_practice = remaining_practice / 2

    result = fri_practice
    return result

print(solution())