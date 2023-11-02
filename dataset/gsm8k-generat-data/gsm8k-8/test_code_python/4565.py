def solution():
    # Calculate the total amount Yoque will pay back
    total_paid = 15 * 11
    
    # Divide the total amount paid by 1.1 to get the original amount borrowed
    original_borrowed = total_paid / 1.1
    result = round(original_borrowed, 2)
    return result

print(solution())