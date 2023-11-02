def solution():
    letters_per_day = 60
    packages_per_day = 20
    days_per_month = 30
    months = 6

    # Calculate the total number of letters received in 6 months
    total_letters = letters_per_day * days_per_month * months

    # Calculate the total number of packages received in 6 months
    total_packages = packages_per_day * days_per_month * months

    # Calculate the total number of pieces of mail handled in 6 months
    total_mail = total_letters + total_packages
    result = total_mail
    return result

print(solution())