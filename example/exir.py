# Import the HollaExAPI class from the lib.py in src derectory, you can copy the file in the example directory
from lib.py  import ExirAPI
# Set your API key and secret
API_KEY = 'your_api_key'
API_SECRET = 'your_secret_key'

# Create an instance of the ExirAPI class with your API key and secret
kit = ExirAPI(api_key=API_KEY, api_secret=API_SECRET)

# Place a sell order for 1 BTC at a price of 1 USDT create_order(market,amount,price,side)
kit.create_order('btc-usdt',1,1,'sell')

# Cancel all orders for the BTC/USDT market
kit.cancel_all_orders('btc-usdt')

# Cancel a specific order with the given order ID
kit.cancel_order('178a1b3b-27d4-4a57-a990-448ac61882cd')

# Get all open orders for the BTC/USDT market
print(kit.get_orders(symbol='btc-usdt'))

# Get a specific order with the given order ID
order = kit.get_order("178a1b3b-27d4-4a57-a990-448ac61882cd")
if order:
    print(order)
else:
    print("Failed to retrieve order.")

# Get all user trades for the BTC/USDT market
print(kit.get_user_trades(symbol='btc-usdt'))

# Withdraw 1 USDT to the specified address on the TRX network
kit.make_withdrawal(currency='usdt', amount=1, address='TFQ9gxeMEkmKoxgrbnHNdu4e3VdNL11vyy', network='trx')

# Get all withdrawals for the BTC currency that are not waiting for confirmation
print(kit.get_withdrawals(currency='btc', waiting='false'))

# Get the balance of XHT in your account
print(kit.get_balance())

# Get user information for your account
print(kit.get_user())

# Get all trades for your account
print(kit.get_trades())

# Get the order book for the BTC/USDT market
orderbooks = kit.get_orderbooks('btc-usdt')
print(orderbooks)

# Get the ticker for the BTC/USDT market
print(kit.get_ticker('btc-usdt'))

# Get all constants for the Exir API
print(kit.get_constants())

# Place a sell order for 1 BTC at a price of 1 USDT
kit.create_order("btc-usdt", 1, 1, "sell")
