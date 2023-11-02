def solution():
    main_job_pay = 20 * 30  # James earns $20 an hour while working at his main job and works 30 hours, thus calculating his earning as 20*30
    second_job_pay = 0.8 * 20 * 15  # James earns 20% less, thus earning $16 per hour at his second job; he works half as much, so 15 hours
    total_pay = main_job_pay + second_job_pay  # Adding both main job and the second job earnings to calculate the total amount James will earn

    result = total_pay
    return result

print(solution())