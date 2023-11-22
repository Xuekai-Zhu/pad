def solution():
    
    # Define the number of customers and the tips per customer
    NUM_CUSTOMERS = 40
    TIPS_PER_CUSTOMER = 20

    # Calculate the total tips
    total_tips = NUM_CUSTOMERS * TIPS_PER_CUSTOMER

    # Calculate the amount of tips Julieta received
    julieta_tips = TIPS_PER_CUSTOMER * 0.9

    # Calculate the total amount of tips Julieta received
    total_julieta_tips = julieta_tips + rafaela_tips

    # Calculate the total amount of tips both Julieta and Rafaela received
    total_received = total_julieta_tips + total_tips

    # Display the total amount of tips
    result = total_received
    return result

print(solution())