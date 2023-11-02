def solution():
    """James earns $20 an hour while working at his main job. He earns 20% less while working his second job. He works 30 hours at his main job and half that much at his second job. How much does he earn per week?"""
    main_job_pay = 20 * 30
    second_job_pay = 0.8 * 20 * 15
    total_pay = main_job_pay + second_job_pay
    result = total_pay
    return result

print(solution())