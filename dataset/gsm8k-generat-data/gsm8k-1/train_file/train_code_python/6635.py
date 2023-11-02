def solution():
    """One dandelion seed floated onto Mrs. Middleton's lawn, landed on good soil, and began to grow. After one month, the dandelion plant had grown to full size and developed a flower. At the end of the second month, the flower turned to 50 fluffy, white seeds, which blew onto the lawn. Only half of these seeds landed onto good soil, germinated, and began to grow, just as the first seed had done. If each of these new seedling plants produces the same number of seeds in the same amount of time as the original plant, what is the total number of seeds that these newest plants will produce in two months' time?"""
    initial_seed_count = 1
    first_month_growth = initial_seed_count * 1
    second_month_growth = first_month_growth * 50 * 0.5
    total_seed_count = initial_seed_count + first_month_growth + second_month_growth + (second_month_growth * 50 * 0.5)
    result = total_seed_count
    return result

print(solution())