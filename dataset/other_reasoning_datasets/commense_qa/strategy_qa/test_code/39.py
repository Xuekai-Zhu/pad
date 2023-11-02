def solution():
    # Define relevant information
    carmine_source = "scale insects that live on a cactus"
    carmine_color = "red"
    carmine_stability = "unstable in oil paints"
    # Check if an oil painter would avoid using reds from the same insect source
    if carmine_source in ["scale insects that live on a cactus"] and carmine_color == "red" and carmine_stability != "stable in oil paints":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())