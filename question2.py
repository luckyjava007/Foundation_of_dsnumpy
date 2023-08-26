import numpy as np

# Create a sample numpy array
arr = np.array([1, 2, 3, 4, 5])

# Check if none of the elements are zero
none_are_zero = np.all(arr != 0)

if none_are_zero:
    print("None of the elements are zero.")
else:
    print("At least one element is zero.")

