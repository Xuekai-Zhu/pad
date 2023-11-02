def solution():
    # Define the method of felting and the recommended washing method for wool
    felting_method = "agitation in soapy water"
    recommended_washing_method = "hand washing"
    # Check if the felting process could potentially damage wool in a washing machine
    if felting_method.lower() in "washer":
        result = "yes"
    else:
        result = "no, but hand washing is recommended"
    return result

print(solution())