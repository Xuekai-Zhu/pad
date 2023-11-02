def solution():
    """Steven's teacher sends the class an assignment to collect 60 different fruit seeds. Apples average 6 seeds, pears average 2 seeds, and grapes average 3 seeds. Steven has set aside 4 apples, 3 pears, and 9 grapes to extract their seeds. How many more seeds does he need to fulfill his assignment?"""
    target_seeds = 60
    apple_seeds = 6
    pear_seeds = 2
    grape_seeds = 3
    extracted_apple_seeds = 4 * apple_seeds
    extracted_pear_seeds = 3 * pear_seeds
    extracted_grape_seeds = 9 * grape_seeds
    total_extracted_seeds = extracted_apple_seeds + extracted_pear_seeds + extracted_grape_seeds
    seeds_left = target_seeds - total_extracted_seeds
    result = seeds_left
    return result

print(solution())