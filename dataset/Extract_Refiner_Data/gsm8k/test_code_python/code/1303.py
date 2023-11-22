def solution():
    
    # Define the number of tables and legs per table
    num_tables = 4
    legs_per_table = 4

    # Define the number of screws needed per leg
    screws_per_leg = 2

    # Calculate the total number of screws needed
    total_screws_needed = num_tables * legs_per_table * screws_per_leg

    # Calculate the number of screws left over
    screws_left_over = 40 - total_screws_needed

    # Display the number of screws left over
    result = screws_left_over
    return result

print(solution())