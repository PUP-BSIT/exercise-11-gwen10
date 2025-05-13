import numpy as np

def generate_random_integers(count, low, high):
    """
    Display a set of random integers and their
    statistical values: mean, median, and standard deviation.
    """
    numbers = np.random.randint(low, high, count) 
    mean = np.mean(numbers)  
    median = np.median(numbers) 
    stddev = np.std(numbers)  

    return numbers, mean, median, stddev

count = 10
low = 1
high = 100

numbers, mean, median, stddev = generate_random_integers(count, low, high)

print("\n-------------------------------------------------------")
print(f"\nGenerated Numbers: {numbers}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {stddev}")
