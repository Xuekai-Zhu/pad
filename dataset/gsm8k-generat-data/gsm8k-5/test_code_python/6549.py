def solution():
    january_amount = 19  # Benny added $19 in January
    february_amount = january_amount  # Benny added the same amount in February
    total_amount = 46  # By the end of March, Benny had $46 in the piggy bank

    # Calculate the amount Benny added to the piggy bank in March
    march_amount = total_amount - january_amount - february_amount
    result = march_amount
    return result

print(solution())