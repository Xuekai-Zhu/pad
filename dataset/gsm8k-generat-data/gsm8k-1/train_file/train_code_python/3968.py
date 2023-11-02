def solution():
    """The teacher decided to rewards his students with extra recess on report card day if they got good grades. Students normally get 20 minutes for recess. He told the students that every A got them 2 extra minutes of recess. Every B got them one extra minute. Every C got them zero extra minutes, but every D got them 1 less minute. When report cards came out there were 10 As, 12 Bs, 14Cs, and 5Ds. In total, how much recess would the students get that day?"""
    base_recess = 20
    extra_A = 2
    extra_B = 1
    reduced_D = -1
    A_count = 10
    B_count = 12
    C_count = 14
    D_count = 5
    total_recess = base_recess + (extra_A * A_count) + (extra_B * B_count) + (reduced_D * D_count)
    result = total_recess
    return result

print(solution())