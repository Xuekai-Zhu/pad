def solution():
    
    total_cups = 27
    num_rows = 3
    cups_per_row = total_cups // num_rows
    remaining_cups = total_cups - cups_per_row
    mint_cups_per_row = remaining_cups // mint_cups_per_row
    result = mint_cups_per_row
    return result

print(solution())