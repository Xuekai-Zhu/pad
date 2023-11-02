def solution():
    """The total average age of three friends is 40. Jared is ten years older than Hakimi, and Molly's age is 30. How old is Hakimi?"""
    total_age = 40 * 3
    molly_age = 30
    jared_age = total_age - molly_age - 10
    hakimi_age = (total_age - molly_age - jared_age) / 1
    result = hakimi_age
    return result

print(solution())