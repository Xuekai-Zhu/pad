def solution():
    
    third_graders = 340
    fourth_graders = 40
    fourth_graders = 100
    fifth_graders = 400
    fourth_pass_rate = fourth_graders * 2
    third_pass_rate = third_graders * 340
    fourth_pass_rate = fourth_graders * 4
    fifth_pass_rate = fourth_pass_rate * fifth_graders
    total_pass_rate = third_pass_rate + fourth_pass_rate + fifth_pass_rate
    result = total_pass_rate
    return result

print(solution())