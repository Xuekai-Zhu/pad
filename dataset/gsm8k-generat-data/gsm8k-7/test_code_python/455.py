def solution():
    num_amoebae = 16
    num_divisions = 4  # because 2^4 = 16

    # Calculate the total number of days needed for one amoeba to reproduce into 16 amoebae
    total_days = num_divisions * 2

    result = total_days
    return result

print(solution())