def solution():
    """Benny has bought a new piggy bank and wants to start saving money. In January he adds $19, then adds the same amount in February. By the end of March, he has $46. How many dollars did he add to the piggy bank in March?"""
    # Define the amount added to the piggy bank in January and February
    amount_added = 19

    # Calculate the total amount in the piggy bank after February
    total_amount_after_feb = amount_added * 2

    # Calculate the amount added in March
    amount_added_in_march = 46 - total_amount_after_feb

    # Display the amount added in March
    result = amount_added_in_march
    return result

print(solution())