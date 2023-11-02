def solution():
    # Define the total number of people
    total_people = 6

    # Calculate the total bill
    total_bill = 150

    # Calculate Silas' payment
    silas_payment = total_bill / 2

    # Calculate the remaining payment
    remaining_payment = total_bill - silas_payment

    # Calculate the total payment with tip
    total_payment_with_tip = remaining_payment * 1.1

    # Calculate how much each of the remaining friends will pay
    each_remaining_friend_payment = total_payment_with_tip / (total_people - 1)
    result = each_remaining_friend_payment
    return result

print(solution())