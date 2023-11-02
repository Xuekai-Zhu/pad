def solution():
    tudor_queens = ["Mary I of England", "Elizabeth I of England", "Margaret Tudor, Queen of Scots"]
    queen_mother_name = "Queen Elizabeth"
    daughter_name = "Queen Elizabeth II"
    mother_daughter_names = [queen_mother_name, daughter_name]
    overlap = [name for name in mother_daughter_names if name in tudor_queens]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())