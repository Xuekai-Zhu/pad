def solution():
    
    # Define the total number of pages in the book
    total_pages = 200

    # Define the number of days the assignment will last
    assignment_days = 30

    # Define the number of pages Mike plans to read per day
    pages_per_day = 10

    # Calculate the total number of days before the deadline
    days_before_deadline = total_pages / pages_per_day

    # Display the number of days before the deadline
    result = days_before_deadline
    return result

print(solution())