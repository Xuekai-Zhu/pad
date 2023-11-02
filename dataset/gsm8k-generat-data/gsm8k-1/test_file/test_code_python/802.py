def solution():
    """Janet is collecting the results of Herbert Hoover Elementary School's annual standardized test. 340 out of 500 third-graders passed, along with 40 out of 100 fourth graders. The 400 fifth graders had a pass rate that was twice the fourth grades' pass rate. What is the school's overall pass rate?"""
    third_graders_passed = 340
    third_graders_total = 500
    fourth_graders_passed = 40
    fourth_graders_total = 100
    fifth_graders_passed = fourth_graders_passed * 2
    fifth_graders_total = 400
    total_passed = third_graders_passed + fourth_graders_passed + fifth_graders_passed
    total_students = third_graders_total + fourth_graders_total + fifth_graders_total
    overall_pass_rate = (total_passed / total_students) * 100
    result = overall_pass_rate
    return result

print(solution())