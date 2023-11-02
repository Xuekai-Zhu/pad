def solution():
    """Calvin has been saving his hair clippings after each haircut to make a wig for his dog. He has gotten 8 haircuts and knows that he needs 2 more to reach his goal. What percentage towards his goal is he?"""
    # Define the number of haircuts Calvin needs to reach his goal
    remaining_haircuts = 2

    # Define the total number of haircuts Calvin has gotten
    total_haircuts = 8

    # Calculate the percentage of haircuts Calvin has towards his goal
    percent = (total_haircuts / (total_haircuts + remaining_haircuts)) * 100

    # return the result
    result = percent
    return result

print(solution())