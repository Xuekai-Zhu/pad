def solution():
    """Conor lives near a beach and loves going there every day to have fun. On a particular week, he found 50 people at the beach on the first day. The next day, 20 more people were present at the beach than on the first day, and on the third day, the total number of people increased to twice the number that were there on the second day. If Conor saw an average of 60 people each day the rest of the week, calculate the total number of people Conor saw at the beach that week."""
    first_day = 50
    second_day = first_day + 20
    third_day = 2 * second_day
    rest_of_week = 4 * 60
    total_people = first_day + second_day + third_day + rest_of_week
    result = total_people
    return result

print(solution())