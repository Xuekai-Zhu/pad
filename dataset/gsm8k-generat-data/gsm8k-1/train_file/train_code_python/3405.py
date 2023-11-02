def solution():
    """Isabelle works in a hotel and runs a bubble bath for each customer who enters the hotel. There are 13 rooms for couples and 14 single rooms. For each bath that is run, Isabelle needs 10ml of bubble bath. If every room is filled to maximum capacity, how much bubble bath, in millilitres, does Isabelle need?"""
    couples_rooms = 13
    single_rooms = 14
    total_customers = (couples_rooms * 2) + single_rooms
    ml_per_bath = 10
    total_ml = total_customers * ml_per_bath
    result = total_ml
    return result

print(solution())