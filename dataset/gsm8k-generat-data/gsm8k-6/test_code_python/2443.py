def solution():
    # Calculate the cost of tickets for Mary and her three children
    total_cost = 2*1 + 3*1  # Mary and her 3 children need tickets, which cost $2 for adults and $1 for children
    change = 20 - total_cost  # Calculate the change Mary will receive using a $20 bill
    result = change
    return result

print(solution())