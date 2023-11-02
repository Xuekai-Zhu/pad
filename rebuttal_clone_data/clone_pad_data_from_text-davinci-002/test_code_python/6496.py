def solution():
    letters_per_day = 60
    packages_per_day = 20
    days_per_month = 30
    months = 6
    total_pieces_of_mail = letters_per_day * packages_per_day * days_per_month * months
    result = total_pieces_of_mail
    return result

print(solution())