def solution():
    # Define the modes of transmission for HIV and contact with silverware
    hiv_transmission = ["blood contact", "mucous membrane contact"]
    silverware_contact = ["saliva contact"]
    # Check if sharing silverware is a mode of HIV transmission
    if set(silverware_contact).issubset(set(hiv_transmission)):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())