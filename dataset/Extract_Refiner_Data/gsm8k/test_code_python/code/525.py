def solution():
    
    # Define the price of the CD and the total amount paid
    CD_PRICE = 4
    TOTAL_PAID = 48

    # Calculate the number of CDs Tom would have been able to buy with his headphone set
    num_cds = TOTAL_PAID / CD_PRICE

    # Calculate the number of CDs Tom would have been able to buy without the headphone set
    num_non_headphone_cds = num_cds - 1

    # Display the number of CDs Tom would have been able to buy with the headphone set
    result = num_non_headphone_cds
    return result

print(solution())