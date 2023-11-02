def solution():
    total_vaccinated = 650
    percent_adults = 0.8  # 80% were adults
    
    # Calculate the number of adults who were vaccinated
    num_adults = total_vaccinated * percent_adults
    
    # Calculate the number of children who were vaccinated
    num_children = total_vaccinated - num_adults
    
    result = num_children
    return result

print(solution())