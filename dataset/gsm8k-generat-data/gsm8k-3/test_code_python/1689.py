def solution():
    """As a freelancer, Baylor is paid for every finished work of a client he does on a freelance marketplace. Currently, he has $4000 on his dashboard from previous work done. He is currently working for three clients, with the first client paying him half the amount of money he currently has on his dashboard once the job is done. The second client will pay him 2/5 times more money than the first client once Baylor finishes his work. The third client will pay him twice the amount of money the first and second clients pay him together once he finishes the job. How much money will Baylor have in his dashboard after all the clients pay him for his work?"""
    # Define the initial amount of money Baylor has in his dashboard
    initial_amount = 4000

    # Calculate the amount of money Baylor will receive from the first client
    first_client_payment = initial_amount / 2

    # Calculate the amount of money Baylor will receive from the second client
    second_client_payment = first_client_payment * (2/5) + first_client_payment

    # Calculate the amount of money Baylor will receive from the third client
    third_client_payment = (first_client_payment + second_client_payment) * 2

    # Calculate the total amount of money Baylor will have in his dashboard
    total_payment = initial_amount + first_client_payment + second_client_payment + third_client_payment

    # Display the total amount of money Baylor will have in his dashboard
    result = total_payment
    return result

print(solution())