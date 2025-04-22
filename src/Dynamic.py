import timeit
import sys
import ast
#function to find minimum coins
def min_count_coins(coins, value): 
    tab = [0] * (value + 1)
    coinUsed = [0] * (value + 1)
    for i in range(value + 1):
        temp = i
        newCoin = 1
        for j in [c for c in coins if c <= i]:
            if tab[i - j]  + 1 < temp:
                temp = tab[i - j]  + 1
                newCoin = j
        tab[i] = temp
        coinUsed[i] = newCoin
    List_Coins = printCoins(coinUsed, value)
    return List_Coins
# function for list of coins used
def printCoins(coinUsed,value):
    coinArr = []
    coin = value
    while coin > 0:
        temp = coinUsed[coin]
        coinArr.append(temp)
        coin = coin - temp
    return coinArr
        
# taking command line arguments
coins = ast.literal_eval(sys.argv[3])
value = int(sys.argv[1])
size = int(sys.argv[2])
# start calculating execution time
start = timeit.default_timer()
list_coins = min_count_coins(coins, value)
end = timeit.default_timer()
#execution time in nanoseconds
execution_time = (end - start)* 1e9
list_coins.reverse()
#output
print(list_coins)
print(execution_time, "nanoseconds")


