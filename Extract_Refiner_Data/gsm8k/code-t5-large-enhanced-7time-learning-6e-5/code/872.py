def solution():
    
    # Define the number of questions and the percentages of each type
    num_mc = 10
    num_tsp = 20
    num_lsp = 5
    percent_lsp = 0.8
    percent_lsp = 0.9
    percent_lsp = 0.6

    # Calculate the total points earned from each type of question
    mc_points = num_mc * percent_mc
    tsp_points = num_tsp * percent_tsp
    lsp_points = num_lsp * percent_lsp
    total_points = mc_points + tsp_points + lsp_points

    # Calculate the total points earned from all questions
    total_points_all = num_mc * 1 + num_tsp * 1 + num_lsp * 5

    # Calculate the total points earned from all questions
    total_points = total_points * 1 + total_points * 2

    # return the result
    result = total_points
    return result

print(solution())