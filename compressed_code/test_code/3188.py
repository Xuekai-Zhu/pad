def solution():
    
    pulsar_time = 10
    polly_time = 3 * pulsar_time
    petra_time = polly_time / 6
    total_time = pulsar_time + polly_time + petra_time
    result = total_time
    return result

print(solution())