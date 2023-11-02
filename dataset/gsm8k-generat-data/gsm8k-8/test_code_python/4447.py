def solution():
    # Define the number of questions of each type and the time it takes to learn each question
    multiple_choice = 30
    fill_in_the_blank = 30
    mc_time = 15
    fitb_time = 25

    # Calculate the total time to learn all multiple-choice questions
    mc_total_time = multiple_choice * mc_time

    # Calculate the total time to learn all fill-in-the-blank questions
    fitb_total_time = fill_in_the_blank * fitb_time

    # Calculate the total time needed to study
    total_time = (mc_total_time + fitb_total_time) / 60

    result = total_time
    return result

print(solution())