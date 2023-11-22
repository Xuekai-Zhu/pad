def solution():
    
    # Define the amount spent on hair
    hair_spending = 400

    # Calculate the amount spent on a manicure
    manicure_spending = hair_spending / 4

    # Calculate the amount spent on a pedicure
    pedicure_spending = manicure_spending * 3 / 4

    # Calculate the total amount spent at the spa
    total_spending = hair_spending + manicure_spending + pedicure_spending

    # Display the total amount spent at the spa
    result = total_spending
    return result

print(solution())