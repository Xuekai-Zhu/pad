def solution():
    """Larry started off having 150 channels from his cable company.  They took 20 channels away and replaced those with 12 channels.  He called the company and asked if he could reduce his package by 10 more channels but add the sports package which is 8 channels.  He realizes that he didn't add the supreme sports package.  He calls back and that package adds 7 more channels.  How many channels does Larry have?"""
    
    # Initial number of channels
    channels = 150
    
    # Account for channels taken away and replaced
    channels -= 20
    channels += 12
    
    # Account for reduction and addition of sports package
    channels -= 10
    channels += 8
    
    # Account for addition of supreme sports package
    channels += 7
    
    # Final number of channels
    result = channels
    
    return result

print(solution())