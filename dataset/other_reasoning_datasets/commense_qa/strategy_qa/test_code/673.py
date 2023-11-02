def solution():
    # Define the countries that American citizens can visit without a passport
    passport_free_countries = ["Northern Mariana Islands"]
    # Check if Mark Cuban can visit Northern Mariana Islands without a passport
    if "Northern Mariana Islands" in passport_free_countries:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())