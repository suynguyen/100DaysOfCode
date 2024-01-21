still_bid = True
auction = {}


def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for key in bidding_record:
        if auction[key] > highest_bid:
            highest_bid = auction[key]
            winner = key
            
    print(f"the winner is {winner}")


while still_bid:
    name = input("What is your name?")
    bid = int(input("Whats is your bid?"))
    auction[name] = bid
    finished_biding = input("Anyone else wants to bid?")
    if finished_biding == "no":
        find_highest_bid(auction)
        still_bid = False
    elif finished_biding == "yes":
        print("next bid")
