import pdb

pdb.set_trace()

user_funds = 10.31
item_price = 8.20

if item_price < user_funds:
    print('you have enough money!')
elif item_price == user_funds:
    print('you have the precise amount of money!')
elif item_price > user_funds:
    print("sorry you don't have enough money?")
