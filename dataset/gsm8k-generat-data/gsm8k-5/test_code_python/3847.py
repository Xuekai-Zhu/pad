def solution():
    # Calculate the number of nice people in each group
    nice_barry = 24  # All people named Barry are nice
    nice_kevin = 0.5 * 20  # Half of people named Kevin are nice
    nice_julie = 0.75 * 80  # Three-fourths of people named Julie are nice
    nice_joe = 0.1 * 50  # 10% of people named Joe are nice

    # Calculate the total number of nice people in the crowd
    total_nice = nice_barry + nice_kevin + nice_julie + nice_joe
    result = total_nice
    return result

print(solution())