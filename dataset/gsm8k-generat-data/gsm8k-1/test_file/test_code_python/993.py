def solution():
    """Walter is collecting money for charity. First he collects $500 from his neighbors. Then he collects $1500 from a fund he set up online. His lawyer offers to donate three times as much as everyone else donates. Walter is going to tell him about his neighbors and the online fund until his friend gives him $200 as well. How much is Walter's lawyer going to contribute?"""
    neighbor_donation = 500
    online_fund_donation = 1500
    total_donation = neighbor_donation + online_fund_donation
    friend_donation = 200
    lawyer_donation = 3 * (total_donation + friend_donation)
    result = lawyer_donation
    
    return result

print(solution())