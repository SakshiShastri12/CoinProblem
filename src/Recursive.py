import timeit
import sys
import ast
# Function to calculate the minimum count of coins
def count_coins(coins, value):
    flag = None
    for c in coins:
        if c == value:
            return c
        if c < value:
            flag = c
    temp = round(value - flag, 2)
    return [flag] + [count_coins(coins, temp)]  # Recursively find the minimum count of coins

output = []

def non_nested(min_coin):
    for i in min_coin:
        if type(i) == list:
            non_nested(i)
        else:
            output.append(i)
    return output
# Function to find the minimum count of coins required
def min_count_coins(coins, value):
    min_coin = count_coins(coins, value)
    res = non_nested(min_coin)
    list_coins = res[::-1]
    # Return the list of coins and its count
    return list_coins, len(list_coins)


coins = ast.literal_eval(sys.argv[3])
value = int(sys.argv[1])
size = int(sys.argv[2])
#start calculating execution time
start = timeit.default_timer()
# Calculate minimum coins required and its count
list_coins, coin_count = min_count_coins(coins, value)
end = timeit.default_timer()
execution_time = (end - start)*1e9  # Calculating the execution time in nanoseconds
# output
print("Coins:", list_coins)
print("Count" , coin_count)
print("Execution time:", execution_time)