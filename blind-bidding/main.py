bids = {}
bidding_finished = False


def check_highest_bidder(bidding_record):
    # bidding record is bids -> being kept track
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        # accessing the value
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner} and they bid ${highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("How much would you like to bid? $"))

    # creating dict with key value pair - name: price (info taken from the input)
    bids[name] = price

    should_continue = input("Are there any other bidders? 'yes' or 'no' ")

    if should_continue == "no":
        bidding_finished = True
        check_highest_bidder(bids)
