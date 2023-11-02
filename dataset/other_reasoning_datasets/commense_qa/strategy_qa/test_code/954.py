def solution():
    golden_gate_bridge_length = 1.7
    stanford_linear_accelerator_length = 2.0
    if stanford_linear_accelerator_length <= golden_gate_bridge_length:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())