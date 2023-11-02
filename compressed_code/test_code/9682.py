def solution():
    
    
    total_mc_questions = 35
    total_ps_questions = 15
    
    
    written_mc_questions = total_mc_questions * (2/5)
    
    
    written_ps_questions = total_ps_questions * (1/3)
    
    
    mc_questions_to_be_written = total_mc_questions - written_mc_questions
    ps_questions_to_be_written = total_ps_questions - written_ps_questions
    
    total_questions_to_be_written = mc_questions_to_be_written + ps_questions_to_be_written
    
    result = total_questions_to_be_written
    
    return result

print(solution())