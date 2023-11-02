def solution():
    calen_pencils_start = 10 + 10  # Calen has 10 left after losing 10, and he originally had 5 more than Caleb
    caleb_pencils_start = calen_pencils_start - 5  # Caleb had 5 less than Calen originally
    candy_pencils_start = (caleb_pencils_start + 3) / 2  # Caleb had 3 less than twice as many as Candy

    # Calculate how many pencils Candy has after Calen lost 10
    candy_pencils_end = candy_pencils_start + 10

    result = candy_pencils_end
    return result

print(solution())