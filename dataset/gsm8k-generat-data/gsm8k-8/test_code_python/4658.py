def solution():
    # Define the total amount Toby's father gave him
    total_amount = 343

    # Calculate the amount each brother received
    brother_amount = total_amount * (1/7)

    # Calculate the total amount Toby gave to his brothers
    total_brother_amount = brother_amount * 2

    # Calculate how much money is left for Toby
    tobys_amount = total_amount - total_brother_amount
    result = tobys_amount
    return result

print(solution())