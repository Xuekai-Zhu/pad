def solution():
    jonathan_first_name = 8
    jonathan_surname = 10

    sister_first_name = 5
    sister_surname = 10

    # Calculate the total number of letters in Jonathan's name
    total_jonathan_letters = jonathan_first_name + jonathan_surname

    # Calculate the total number of letters in his sister's name
    total_sister_letters = sister_first_name + sister_surname

    # Calculate the total number of letters in both names
    total_letters = total_jonathan_letters + total_sister_letters
    result = total_letters
    return result

print(solution())