def solution():
    """A carpenter made ten tables for this month. Last month, he made three fewer tables than this month. How many tables did the carpenter make in total?"""
    # Define the number of tables made this month and last month
    this_month_tables = 10
    last_month_tables = this_month_tables - 3

    # Calculate the total number of tables made
    total_tables = this_month_tables + last_month_tables

    # Display the total number of tables made
    result = total_tables
    return result

print(solution())