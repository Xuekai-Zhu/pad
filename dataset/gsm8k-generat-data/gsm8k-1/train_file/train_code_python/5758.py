def solution():
    """Jonathan's full name contains 8 letters for the first name and 10 letters for the surname. His sister's name has 5 letters for the first name and 10 letters for the second name. What's the total number of letters in their names?"""
    jonathan_first_name_letters = 8
    jonathan_surname_letters = 10
    sister_first_name_letters = 5
    sister_surname_letters = 10
    
    total_letters = jonathan_first_name_letters + jonathan_surname_letters + sister_first_name_letters + sister_surname_letters
    result = total_letters
    
    return result

print(solution())