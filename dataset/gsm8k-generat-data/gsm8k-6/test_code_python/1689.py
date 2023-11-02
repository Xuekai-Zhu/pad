def solution():
    # Calculate the amount of money the first client will pay Baylor
    client_one_payment = 4000/2  

    # Calculate the amount of money the second client will pay Baylor
    client_two_payment = 2/5 * client_one_payment + client_one_payment  

    # Calculate the total amount of money the first two clients will pay Baylor
    first_two_clients_payment = client_one_payment + client_two_payment  

    # Calculate the amount of money the third client will pay Baylor
    client_three_payment = 2 * first_two_clients_payment  

    # Calculate the total amount of money Baylor will have in his dashboard after all the clients pay him
    total_payment = client_one_payment + client_two_payment + client_three_payment + 4000  

    result = total_payment
    return result

print(solution())