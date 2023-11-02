def solution():
    """Mara has 40 crayons and 10 percent of her crayons are pink. Luna has 50 crayons and 20 percent of them are pink. In total how many pink crayons do Mara and Luna have?"""
    # Define the initial number of crayons and the percentage of pink crayons
    mara_crayons = 40
    luna_crayons = 50
    mara_pink_perc = 0.10
    luna_pink_perc = 0.20

    # Calculate the number of pink crayons for each person
    mara_pink = mara_crayons * mara_pink_perc
    luna_pink = luna_crayons * luna_pink_perc

    # Calculate the total number of pink crayons
    total_pink = mara_pink + luna_pink

    # return the result
    result = total_pink
    return result

print(solution())