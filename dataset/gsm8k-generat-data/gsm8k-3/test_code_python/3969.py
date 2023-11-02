def solution():
    """The teacher decided to rewards his students with extra recess on report card day if they got good grades. Students normally get 20 minutes for recess. He told the students that every A got them 2 extra minutes of recess. Every B got them one extra minute. Every C got them zero extra minutes, but every D got them 1 less minute. When report cards came out there were 10 As, 12 Bs, 14Cs, and 5Ds. In total, how much recess would the students get that day?"""
    # Define the base recess time in minutes
    BASE_RECESS_TIME = 20

    # Define the number of extra minutes for each grade
    A_EXTRA_MINUTES = 2
    B_EXTRA_MINUTES = 1
    C_EXTRA_MINUTES = 0
    D_EXTRA_MINUTES = -1

    # Calculate the total extra recess time in minutes
    total_extra_minutes = (10 * A_EXTRA_MINUTES) + (12 * B_EXTRA_MINUTES) + (5 * D_EXTRA_MINUTES)

    # Calculate the total recess time in minutes
    total_recess_time = BASE_RECESS_TIME + total_extra_minutes

    # Display the total recess time
    result = total_recess_time
    return result

print(solution())