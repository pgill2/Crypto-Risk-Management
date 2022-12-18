
# imports 
import ccxt
import time



# exchange object 
exchange = ccxt.binanceusdm({'timeout': 20000})

# we can then connect our account (binance)
exchange_id = 'Binance'
exchange_class = getattr(ccxt, exchange_id)

exchange = exchange_class ({
    
    'apiKey': 'ADD API KEY HERE',
    'secret': 'ADD YOUR SECRET HERE',
    'options': {'defaultType': 'future'},
    'enableRateLimit': True,

})

print('\nLogin Successful\n')


while True:

    # get list (Binance)

    symbols = exchange.load_markets()

    # iterate over each symbol 
    for symbol in symbols:

        # set leverage
        exchange.set_leverage(3, symbol)

    print('Leverage set')

    time.sleep(5)









































