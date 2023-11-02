def solution():
    # Number of puppies adopted each week
    week1 = 20
    week2 = (2/5) * week1
    week3 = 2 * week2
    week4 = week1 + 10

    # Total number of puppies adopted in one month
    total_puppies = week1 + week2 + week3 + week4

    result = total_puppies
    return result

print(solution())