def solution():
    book_setting = "Connecticut"
    setting_in_major_city = False
    book_location = "Revolutionary Hill Estates"
    if book_setting == "Connecticut" and not setting_in_major_city and book_location == "Revolutionary Hill Estates":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())