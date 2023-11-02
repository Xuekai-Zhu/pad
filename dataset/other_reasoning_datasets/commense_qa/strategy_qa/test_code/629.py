def solution():
    frigate_features = ["sails", "masts", "rigging"]
    rope_required_features = ["sails", "rigging"]
    rope_required = all(feature in rope_required_features for feature in frigate_features)
    if rope_required:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())