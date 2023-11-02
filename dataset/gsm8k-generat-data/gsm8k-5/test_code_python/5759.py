def solution():
    # Calculate the total number of letters in Jonathan's name
    jonathan_first_name = 8  # Jonathan's first name has 8 letters
    jonathan_surname = 10  # Jonathan's surname has 10 letters
    jonathan_total = jonathan_first_name + jonathan_surname

    # Calculate the total number of letters in Jonathan's sister's name
    sister_first_name = 5  # Jonathan's sister's first name has 5 letters
    sister_surname = 10  # Jonathan's sister's surname has 10 letters
    sister_total = sister_first_name + sister_surname

    # Calculate the total number of letters in both names
    total_letters = jonathan_total + sister_total
    result = total_letters
    return result

print(solution())