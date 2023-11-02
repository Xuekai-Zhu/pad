def solution():
    # Calculate the total amount of bubble bath needed
    couples_baths = 13 * 2  # 13 rooms for couples with 2 customers each
    single_baths = 14  # 14 single rooms with 1 customer each
    total_baths = couples_baths + single_baths  # total number of baths
    total_bubble_bath = total_baths * 10  # 10ml of bubble bath needed for each bath
    result = total_bubble_bath
    return result

print(solution())