def solution():
    # Calculate the total number of books borrowed
    total_borrowed = 100 - 60  # 60 books remained on the shelf by the evening
    # Calculate the number of books borrowed between lunchtime and evening
    afternoon_borrowed = total_borrowed - 40  # Hadley added 40 more books after lunchtime
    result = afternoon_borrowed
    return result

print(solution())