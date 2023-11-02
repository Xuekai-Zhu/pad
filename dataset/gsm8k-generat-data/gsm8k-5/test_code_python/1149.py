def solution():
    age_initial = 6  # Mandy started reading books when she was 6 years old
    pages_initial = 8  # The first books she read had 8 pages

    age_twice_initial = age_initial * 2  # Mandy was twice her initial age when she started reading books 5 times longer
    pages_twice_initial = pages_initial * 5  # The books she read then were 5 times longer than the initial books

    age_present = age_twice_initial + 8  # Mandy is 8 years older than when she started reading books that were 5 times longer
    pages_present = pages_twice_initial * 4  # The books she reads now are 4 times longer than the books she read when she was twice her initial age

    result = pages_present
    return result

print(solution())