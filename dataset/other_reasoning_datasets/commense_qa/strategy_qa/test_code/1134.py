def solution():
    # Define basic emotion and frog vocalization types
    basic_emotions = ["anger", "disgust", "fear", "happiness", "sadness", "surprise"]
    frog_vocalizations = ["advertisement calls", "agonistic calls", "distress calls", "release calls"]
    # Check if disgust is a basic emotion and if there are frog vocalizations associated with disgust
    if "disgust" in basic_emotions and any("disgust" in call for call in frog_vocalizations):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())