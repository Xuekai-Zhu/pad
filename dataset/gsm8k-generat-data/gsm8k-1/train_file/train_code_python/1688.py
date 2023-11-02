def solution():
    """As a freelancer, Baylor is paid for every finished work of a client he does on a freelance marketplace. Currently, he has $4000 on his dashboard from previous work done. He is currently working for three clients, with the first client paying him half the amount of money he currently has on his dashboard once the job is done. The second client will pay him 2/5 times more money than the first client once Baylor finishes his work. The third client will pay him twice the amount of money the first and second clients pay him together once he finishes the job. How much money will Baylor have in his dashboard after all the clients pay him for his work?"""
    current_balance = 4000
    first_payment = current_balance / 2
    second_payment = first_payment * (2/5) + first_payment
    third_payment = (first_payment + second_payment) * 2
    total_payment = first_payment + second_payment + third_payment
    new_balance = current_balance + total_payment
    result = new_balance
    return result

print(solution())