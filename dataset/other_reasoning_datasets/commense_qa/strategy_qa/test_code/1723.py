def solution():
    # Define the characteristics of Darth Vader and Severus Snape
    vader_appearance = ["black full-body armor", "mask"]
    snape_appearance = ["white man", "long greasy black hair", "cloak"]
    # Check if Vader's appearance resembles Snape's
    if set(vader_appearance).issubset(snape_appearance):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())