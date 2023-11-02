def solution():
    # Calculate the number of times the amoeba needs to divide to reach 16 amoebae
    num_divisions = 4 # Each division doubles the number of amoebae. 2^4 = 16
    days_to_divide = num_divisions * 2 # Each division takes 2 days
    result = days_to_divide
    return result

print(solution())