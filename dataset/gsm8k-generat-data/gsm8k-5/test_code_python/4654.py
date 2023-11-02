def solution():
    total_years = 70  # Tom and Devin have been teaching for a total of 70 years

    # Let's define Tom's years of teaching as x
    # Then, Devin's years of teaching can be expressed as (0.5x - 5)
    # And, their total years of teaching is x + (0.5x - 5) = 1.5x - 5
    
    # Solve for x
    x = (total_years + 5) / 1.5
    result = x
    return result

print(solution())