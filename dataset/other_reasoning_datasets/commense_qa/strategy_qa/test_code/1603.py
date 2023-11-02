def solution():
    # Define where Arnold Schwarzenegger was born and the requirement for running for US President
    arnold_birthplace = "Austria"
    presidential_requirement = "born in the USA"
    # Check if Arnold meets the requirement for running for US President
    if arnold_birthplace != presidential_requirement:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())