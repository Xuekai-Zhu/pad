def solution():
    mp3_format = "audio"
    golden_gate_bridge_sound = "yes"
    if golden_gate_bridge_sound and mp3_format == "audio":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())