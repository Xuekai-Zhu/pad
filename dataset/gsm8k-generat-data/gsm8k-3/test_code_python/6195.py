def solution():
    """Mara has 40 crayons and 10 percent of her crayons are pink. Luna has 50 crayons and 20 percent of them are pink. In total how many pink crayons do Mara and Luna have?"""
    # Calculate the number of pink crayons Mara has
    mara_pink = round(0.1 * 40)

    # Calculate the number of pink crayons Luna has
    luna_pink = round(0.2 * 50)

    # Calculate the total number of pink crayons
    total_pink = mara_pink + luna_pink

    # Display the total number of pink crayons
    result = total_pink
    return result

print(solution())