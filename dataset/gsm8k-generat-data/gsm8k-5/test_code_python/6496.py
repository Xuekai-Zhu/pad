def solution():
    letters_per_day = 60  # The post office receives 60 letters per day
    packages_per_day = 20  # The post office receives 20 packages per day
    days_per_month = 30  # There are 30 days in each month
    months = 6  # We want to know how much mail the post office handles in 6 months

    # Calculate the total pieces of mail handled by the post office in 6 months
    total_mail = (letters_per_day + packages_per_day) * days_per_month * months
    result = total_mail
    return result

print(solution())