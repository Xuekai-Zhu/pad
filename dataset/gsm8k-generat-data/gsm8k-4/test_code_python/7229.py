def solution():
    """Alex has some new shirts. Joe has 3 more new shirts than Alex. Ben has eight more new shirts than Joe. If Ben has 15 new shirts, how many new shirts does Alex have?"""
    # Define the number of new shirts Ben has
    ben_shirts = 15

    # Calculate the number of new shirts Joe has
    joe_shirts = ben_shirts - 8

    # Calculate the number of new shirts Alex has
    alex_shirts = joe_shirts - 3

    result = alex_shirts
    return result

print(solution())