def solution():
    # Amount collected from friend
    friend_payment = 5 * 7  # $5 per day, for 7 days

    # Amount collected from brother
    brother_payment = 8 * 7  # $8 per day, for 7 days

    # Amount collected from cousin
    cousin_payment = 4 * 7  # $4 per day, for 7 days

    # Total amount collected in 7 days
    total_collection = friend_payment + brother_payment + cousin_payment
    result = total_collection
    return result

print(solution())