def solution():
    # Define the type of virus COVID-19 is categorized under
    virus_type = "RNA"
    # Check if whole genome sequencing can be used for COVID-19
    if virus_type != "DNA":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())