def solution():
    # Calculate the total number of bubble baths needed for the couples rooms
    couples_baths = 13 * 2  # There are 13 rooms for couples with 2 people in each room
    couples_bubble_bath = couples_baths * 10  # Isabelle needs 10ml of bubble bath for each couple's bath

    # Calculate the total number of bubble baths needed for the single rooms
    single_baths = 14 * 1  # There are 14 single rooms with 1 person in each room
    single_bubble_bath = single_baths * 10  # Isabelle needs 10ml of bubble bath for each single's bath

    # Calculate the total amount of bubble bath needed
    total_bubble_bath = couples_bubble_bath + single_bubble_bath
    result = total_bubble_bath
    return result

print(solution())