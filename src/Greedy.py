import timeit
import sys
import ast
# Function to find the minimum count of coins
def min_count_coins(coins, value):
	n = len(coins)
	i = n - 1
	List_Coins = [] # Initializing an empty list
	while( i >= 0):
		while( value >= coins[i]):
			value -= coins[i]
			List_Coins.append(coins[i]) # Adding the coin to the list
		i -= 1

	return List_Coins # Return the list of coins use



coins = ast.literal_eval(sys.argv[3])
value = int(sys.argv[1])
size = int(sys.argv[2])
# starting to measure the execution time
start = timeit.default_timer()
list_coins = min_count_coins(coins, value)
end = timeit.default_timer()
# execution time in nanoseconds
execution_time = (end - start)*1e9
#Output
print(list_coins)
print(execution_time , "nanoseconds")