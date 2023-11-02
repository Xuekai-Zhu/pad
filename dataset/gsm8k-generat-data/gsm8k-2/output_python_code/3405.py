def solution():
    """Isabelle works in a hotel and runs a bubble bath for each customer who enters the hotel. There are 13 rooms for couples and 14 single rooms. For each bath that is run, Isabelle needs 10ml of bubble bath. If every room is filled to maximum capacity, how much bubble bath, in millilitres, does Isabelle need?"""
    couples_rooms = 13
    single_rooms = 14
    total_rooms = couples_rooms + single_rooms
    ml_per_bath = 10
    total_baths = couples_rooms * 2 + single_rooms
    total_ml_needed = total_baths * ml_per_bath
    result = total_ml_needed
    return result

print(solution())