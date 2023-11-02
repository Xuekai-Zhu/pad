def solution():
    # Calculate the number of puppies adopted by Yuri in each week
    week1 = 20
    week2 = (2/5) * week1
    week3 = 2 * week2
    week4 = week1 + 10

    # Calculate the total number of puppies adopted by Yuri
    total_puppies = week1 + week2 + week3 + week4
    result = total_puppies
    return result

print(solution())