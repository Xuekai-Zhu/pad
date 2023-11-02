def solution():
    """Alex has some new shirts. Joe has 3 more new shirts than Alex. Ben has eight more new shirts than Joe. If Ben has 15 new shirts, how many new shirts does Alex have?"""
    # Determine Joe's number of new shirts
    joe_shirts = 15 - 8 - 3

    # Determine Alex's number of new shirts
    alex_shirts = joe_shirts - 3

    # Display Alex's number of new shirts
    result = alex_shirts
    return result

print(solution())