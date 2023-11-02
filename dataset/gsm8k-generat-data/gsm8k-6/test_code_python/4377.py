def solution():
    # Calculate the number of pencils originally had by Calen and Caleb
    calen_initial = 10 + 10  # Calen lost 10 pencils and has 10 now, so he originally had 20
    caleb_initial = calen_initial - 5  # Calen originally had 5 more than Caleb, so Caleb had 15

    # Calculate the number of pencils Candy has
    candy_initial = (caleb_initial + 3) / 2  # Caleb has 3 less than twice as many pencils as Candy
    result = candy_initial
    return result

print(solution())