def solution():
    """As a freelancer, Baylor is paid for every finished work of a client he does on a freelance marketplace. Currently, he has $4000 on his dashboard from previous work done. He is currently working for three clients, with the first client paying him half the amount of money he currently has on his dashboard once the job is done.
    The second client will pay him 2/5 times more money than the first client once Baylor finishes his work. The third client will pay him twice the amount of money the first and second clients pay him together once he finishes the job. How much money will Baylor have in his dashboard after all the clients pay him for his work?"""
    # Define the initial amount of money on Baylor's dashboard
    initial_amount = 4000

    # Calculate the payment from the first client
    first_client_payment = initial_amount / 2

    # Calculate the payment from the second client
    second_client_payment = first_client_payment * (2/5) + first_client_payment

    # Calculate the payment from the third client
    third_client_payment = (first_client_payment + second_client_payment) * 2

    # Calculate the total payment Baylor will receive
    total_payment = first_client_payment + second_client_payment + third_client_payment

    # Calculate the final amount of money on Baylor's dashboard
    final_amount = initial_amount + total_payment

    # Return the final amount
    result = final_amount
    return result

print(solution())