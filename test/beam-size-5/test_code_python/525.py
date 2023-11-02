def solution():
    
    # Define the cost of the headphone set and the total amount paid
    HEADPHONE_SET_COST = 4
    TOTAL_PAID = 48

    # Calculate the amount of CDs Tom can buy with the headphone set
    headphone_cds = TOTAL_PAID - HEADPHONE_SET_COST

    # Calculate the number of CDs Tom can buy with the headphone set
    cds_bought = headphone_cds // 4

    # Display the number of CDs Tom can buy
    result = cds_bought
    return result

print(solution())