def solution():
    # Calculate the number of pieces of shepherd's pie per customer
    shepherd_pieces_per_customer = 4 / 1

    # Calculate the number of pieces of chicken pot pie per customer
    chicken_pieces_per_customer = 5 / 1

    # Calculate the total number of shepherd's pie pieces sold
    total_shepherd_pieces = 52 * shepherd_pieces_per_customer

    # Calculate the total number of chicken pot pie pieces sold
    total_chicken_pieces = 80 * chicken_pieces_per_customer

    # Calculate the total number of pies sold
    total_pies = (total_shepherd_pieces + total_chicken_pieces) / (shepherd_pieces_per_customer + chicken_pieces_per_customer)
    result = total_pies
    return result

print(solution())