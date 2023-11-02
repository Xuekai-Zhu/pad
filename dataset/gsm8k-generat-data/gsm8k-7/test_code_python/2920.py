def solution():
    total_age = 3 * 40  # Total age of three friends
    molly_age = 30  # Molly's age
    jared_age = molly_age + 10  # Jared is ten years older than Hakimi
    hakimi_age = (total_age - jared_age - molly_age) / 1  # Solve for Hakimi's age
    result = hakimi_age
    return result

print(solution())