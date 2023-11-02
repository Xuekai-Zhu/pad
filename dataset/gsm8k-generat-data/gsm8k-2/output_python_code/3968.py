def solution():
    """The teacher decided to rewards his students with extra recess on report card day if they got good grades. Students normally get 20 minutes for recess. He told the students that every A got them 2 extra minutes of recess. Every B got them one extra minute. Every C got them zero extra minutes, but every D got them 1 less minute. When report cards came out there were 10 As, 12 Bs, 14Cs, and 5Ds. In total, how much recess would the students get that day?"""
    base_recess_time = 20
    extra_time_per_A = 2
    extra_time_per_B = 1
    less_time_per_D = 1
    total_extra_time = (10 * extra_time_per_A) + (12 * extra_time_per_B) - (5 * less_time_per_D)
    total_recess_time = base_recess_time + total_extra_time
    result = total_recess_time
    return result

print(solution())