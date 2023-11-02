def solution():
    """Jonathan was sad to learn he needed 2 more toys than he already had to have enough toys to make a sorted play set five times larger than James's play set, which had 80 toys. How many toys does Jonathan currently have?"""
    james_toys = 80
    jonathan_extra_toys = 2
    sorted_playset_size = 5
    total_jonathan_toys = james_toys * sorted_playset_size + jonathan_extra_toys
    current_jonathan_toys = total_jonathan_toys - jonathan_extra_toys
    result = current_jonathan_toys
    return result

print(solution())