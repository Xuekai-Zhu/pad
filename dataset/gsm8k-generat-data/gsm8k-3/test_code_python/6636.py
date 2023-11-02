def solution():
    """One dandelion seed floated onto Mrs. Middleton's lawn, landed on good soil, and began to grow.  After one month, the dandelion plant had grown to full size and developed a flower.  At the end of the second month, the flower turned to 50 fluffy, white seeds, which blew onto the lawn.  Only half of these seeds landed onto good soil, germinated, and began to grow, just as the first seed had done.  If each of these new seedling plants produces the same number of seeds in the same amount of time as the original plant, what is the total number of seeds that these newest plants will produce in two months' time?"""
    # Define the initial number of seeds
    initial_seeds = 1

    # After one month, the initial seed has grown to a full plant and developed a flower
    # which turns into 50 fluffy, white seeds
    first_month_seeds = 50

    # Half of these new seeds germimate and grow into new plants
    second_month_plants = first_month_seeds // 2

    # Each of these new plants produces 50 new seeds at the end of the second month
    second_month_seeds = second_month_plants * 50

    # The total number of seeds produced by all the plants at the end of the second month
    total_seeds = initial_seeds + first_month_seeds + second_month_seeds

    # Display the total number of seeds
    result = total_seeds
    return result

print(solution())