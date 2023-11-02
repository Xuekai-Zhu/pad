def solution():
    """The post office receives 60 letters and 20 packages per day. How many pieces of mail does it handle in six months if all the months have 30 days?"""
    # Define the number of days in six months and the number of mail received per day
    DAYS_PER_MONTH = 30
    TOTAL_MONTHS = 6
    LETTERS_PER_DAY = 60
    PACKAGES_PER_DAY = 20

    # Calculate the total amount of mail received in six months
    total_letters = LETTERS_PER_DAY * DAYS_PER_MONTH * TOTAL_MONTHS
    total_packages = PACKAGES_PER_DAY * DAYS_PER_MONTH * TOTAL_MONTHS
    total_mail = total_letters + total_packages

    # return the result
    result = total_mail
    return result

print(solution())