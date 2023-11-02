def solution():
    """Jackson is buying school supplies for his third grade class, which has 30 students. Each student needs 5 pens, 3 notebooks, 1 binder and 2 highlighters. Pens cost $0.50, notebooks cost $1.25, binders cost $4.25, and highlighters cost $0.75. If Jackson gets a $100 teacher discount, how much does he spend on school supplies?"""
    # Define the number of students and the required items per student
    NUM_STUDENTS = 30
    PENS_PER_STUDENT = 5
    NOTEBOOKS_PER_STUDENT = 3
    BINDERS_PER_STUDENT = 1
    HIGHLIGHTERS_PER_STUDENT = 2

    # Define the cost of each item
    PEN_PRICE = 0.5
    NOTEBOOK_PRICE = 1.25
    BINDER_PRICE = 4.25
    HIGHLIGHTER_PRICE = 0.75

    # Calculate the total number of items needed
    total_pens = NUM_STUDENTS * PENS_PER_STUDENT
    total_notebooks = NUM_STUDENTS * NOTEBOOKS_PER_STUDENT
    total_binders = NUM_STUDENTS * BINDERS_PER_STUDENT
    total_highlighters = NUM_STUDENTS * HIGHLIGHTERS_PER_STUDENT

    # Calculate the total cost of each item
    pens_cost = total_pens * PEN_PRICE
    notebooks_cost = total_notebooks * NOTEBOOK_PRICE
    binders_cost = total_binders * BINDER_PRICE
    highlighters_cost = total_highlighters * HIGHLIGHTER_PRICE

    # Calculate the total cost of all the items
    total_cost = pens_cost + notebooks_cost + binders_cost + highlighters_cost - 100  # subtract the teacher discount

    # Display the total cost
    result = total_cost
    return result

print(solution())