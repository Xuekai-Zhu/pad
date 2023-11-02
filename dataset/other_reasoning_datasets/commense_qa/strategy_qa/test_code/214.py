def solution():
    # Define the religions that believe in the Second Coming
    religions_with_second_coming = ["Christianity", "Islam"]
    # Define Woody Allen's religion
    woody_allen_religion = "Judaism"
    # Check if Woody Allen's religion believes in the Second Coming
    if woody_allen_religion not in religions_with_second_coming:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())