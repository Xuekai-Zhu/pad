def solution():
    # Calculate the total cost of buying one reading book for every student
    book_cost_per_student = 12 * 30 
    
    # Determine if Sally needs to pay out of pocket and calculate the amount
    if book_cost_per_student > 320:
        amount_out_of_pocket = book_cost_per_student - 320
    else:
        amount_out_of_pocket = 0
    
    result = amount_out_of_pocket
    return result

print(solution())