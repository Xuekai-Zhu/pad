def solution():
    # Find the total age of Jared, Hakimi, and Molly
    total_age = 40 * 3  # since the total average age of the three friends is 40

    # Find Jared's age
    jared_age = 30 + 10  # Jared is ten years older than Hakimi

    # Find the age of Hakimi
    hakimi_age = (total_age - jared_age - 30) / 1  # subtract Jared and Molly's age from total and divide by 1 since there are only 3 people

    result = hakimi_age
    return result

print(solution())