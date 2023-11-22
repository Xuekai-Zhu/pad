def solution():
    
    # Define the cost per lollypop and the number of students
    COST_PER_LOLLIPOP = 0.8
    NUM_STUDENTS = 30

    # Define the number of lollipops sold per student
    NUM_LOLLIPS_PER_STUDENT = 10

    # Define the cost per lollipop and the cost per lollipop
    COST_PER_LOLLIPOP = 0.5

    # Calculate the total cost of all lollipops sold
    total_cost = COST_PER_LOLLIPOP * NUM_STUDENTS

    # Calculate the total revenue from selling lollipops
    total_revenue = NUM_LOLLIPS_PER_STUDENT * NUM_LOLLIPS_PER_STUDENT * COST_PER_LOLLIPOP

    # Calculate the profit from selling lollipops
    profit = total_revenue - total_cost

    # Display the profit
    result = profit

print(solution())