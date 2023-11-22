def solution():
    
    # Define the minimum amounts for each person
    student_loan_minimum = 300
    credit_card_minimum = 200
    mortgage_minimum = 500

    # Calculate the total minimum amounts for a year
    total_minimum = student_loan_minimum + credit_card_minimum + mortgage_minimum

    # Calculate the amount Jessica wants to pay in a year
    additional_payment = total_minimum * 0.5

    # Calculate the total amount Jessica will pay in a year
    total_payment = total_minimum * 12 + additional_payment

    # Display the total amount Jessica will pay in a year
    result = total_payment
    return result

print(solution())