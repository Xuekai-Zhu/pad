def solution():
    initial_dashboard_money = 4000
    client1_payment = initial_dashboard_money / 2
    client2_payment = client1_payment * (2/5) + client1_payment
    client3_payment = (client1_payment + client2_payment) * 2

    total_payment = client1_payment + client2_payment + client3_payment
    final_dashboard_money = initial_dashboard_money + total_payment
    result = final_dashboard_money
    return result

print(solution())