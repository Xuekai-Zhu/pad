def solution():
    # Set the initial assumption of Hades' grip on the Underworld as tight
    hades_grip = "tight"
    # Consider the fact that Hades has complete control over the subjects in the Underworld
    if hades_grip == "tight":
        # If Hades has complete control over the subjects, his grip is tight
        result = "no"
    else:
        # Otherwise, his grip is loose
        result = "yes"
    return result

print(solution())