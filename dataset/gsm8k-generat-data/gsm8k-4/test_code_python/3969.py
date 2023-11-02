def solution():
    """The teacher decided to rewards his students with extra recess on report card day if they got good grades. Students normally get 20 minutes for recess. He told the students that every A got them 2 extra minutes of recess. Every B got them one extra minute. Every C got them zero extra minutes, but every D got them 1 less minute. When report cards came out there were 10 As, 12 Bs, 14Cs, and 5Ds. In total, how much recess would the students get that day?"""
    # Define the number of students who received each grade
    num_As = 10
    num_Bs = 12
    num_Cs = 14
    num_Ds = 5

    # Define the number of extra minutes earned for each grade
    As_extra_min = 2
    Bs_extra_min = 1
    Cs_extra_min = 0
    Ds_extra_min = -1

    # Calculate the total number of extra minutes earned
    total_extra_min = (num_As * As_extra_min) + (num_Bs * Bs_extra_min) + (num_Ds * Ds_extra_min)

    # Add the total extra minutes to the normal recess time of 20 minutes
    total_recess_min = 20 + total_extra_min

    result = total_recess_min
    return result

print(solution())