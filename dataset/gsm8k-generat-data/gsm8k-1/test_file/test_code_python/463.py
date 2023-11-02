Unfortunately, we cannot provide a solution to the Samantha's last name question as it is incomplete and does not provide enough information to answer the question. 

Here's a possible solution for the laundry question: 

def solution():
    """Bob is in charge of doing laundry for a large hotel. Each room has two sheets, one comforter, twice as many pillow cases as sheets and twice as many towels as pillow cases. How many pieces of laundry are there in 80 rooms?"""
    num_sheets = 2
    num_comforters = 1
    num_pillowcases = num_sheets * 2
    num_towels = num_pillowcases * 2
    total_pieces = (num_sheets + num_comforters + num_pillowcases + num_towels) * 80
    result = total_pieces
    return result

print(solution())