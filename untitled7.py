# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z9sFQxF4KbINvAlvVBq_ahx9o_x-UN8C
"""

import numpy as np
import pandas as pd

# 1. Create a NumPy array 'arr' of integers from 0 to 5 and print its data type.
arr = np.arange(6)
print("Array:", arr)
print("Data type:", arr.dtype)



# 2. Check if the data type of 'arr' is float64.
arr = np.array([1.0, 2.0, 3.0], dtype=np.float64)

is_float64 = arr.dtype == np.float64
print("Is 'arr' of type float64?", is_float64)

# 3. Create a NumPy array 'arr' with a data type of complex128 containing three complex numbers.
complex_arr = np.array([1+2j, 3+4j, 5+6j], dtype=np.complex128)
print("Complex array:", complex_arr)

# 4. Convert an existing NumPy array 'arr' of integers to float32 data type.
arr_float32 = arr.astype(np.float32)
print("Array converted to float32:", arr_float32)

# 5. Convert a NumPy array 'arr' of float64 to float32 to reduce decimal precision.
arr_float64 = np.array([1.1, 2.2, 3.3], dtype=np.float64)
arr_reduced_precision = arr_float64.astype(np.float32)
print("Array with reduced precision:", arr_reduced_precision)

# 6. Function to return shape, size, and data type of an array.
def array_attributes(array):
    return array.shape, array.size, array.dtype

print("Array attributes:", array_attributes(arr))

# 7. Function to return the dimensionality of an array.
def array_dimension(array):
    return array.ndim

print("Array dimension:", array_dimension(arr))

# 8. Function to return the item size and total size in bytes of an array.
def item_size_info(array):
    return array.itemsize, array.nbytes

print("Item size and total size in bytes:", item_size_info(arr))

# 9. Create a function array_strides that takes a NumPy array as input and returns the strides of the array.
def array_strides(array):
    return array.strides
print (array_strides(arr))

# 10. Design a function shape_stride_relationship that takes a NumPy array as input and returns the shape and strides of the array.
def shape_stride_relationship(array):
    return array.shape, array.strides
print(shape_stride_relationship(arr))

# 11. Create a function `create_zeros_array` that takes an integer `n` as input and returns a NumPy array of zeros with `n` elements.
def create_zeros_array(n):
    return np.zeros(n)

print(create_zeros_array(5))

# 12. Write a function `create_ones_matrix` that takes integers `rows` and `cols` as inputs and generates a 2D NumPy array filled with ones of size `rows x cols`.
def create_ones_matrix(rows, cols):
    return np.ones((rows, cols))

print(create_ones_matrix(3, 4))

# 13. Write a function `generate_range_array` that takes three integers start, stop, and step as arguments and creates a NumPy array with a range.
def generate_range_array(start, stop, step):
    return np.arange(start, stop, step)

print (generate_range_array(1, 10, 2))

# 14. Design a function `generate_linear_space` that takes two floats `start`, `stop`, and an integer `num`.
def generate_linear_space(start, stop, num):
    return np.linspace(start, stop, num)

print(generate_linear_space(0.0, 1.0, 5))

# 15. Create a function `create_identity_matrix` that takes an integer `n` as input and generates a square identity matrix.
def create_identity_matrix(n):
    return np.eye(n)

print(create_identity_matrix(3))

# 16. Write a function that takes a Python list and converts it into a NumPy array.
def list_to_numpy_array(py_list):
    return np.array(py_list)

print(list_to_numpy_array([1, 2, 3, 4]))

# 17. Create a NumPy array and demonstrate the use of `numpy.view` to create a new array object with the same data.
arr = np.array([1.5, 2.6, 3.7])
arr_view = arr.view()
print(arr_view)

# 18. Function to concatenate two NumPy arrays along a specified axis.
def concatenate_arrays(arr1, arr2, axis=0):
    return np.concatenate((arr1, arr2), axis=axis)

print(concatenate_arrays(np.array([1, 2, 3]), np.array([2, 3, 5])))

# 19. Concatenate two NumPy arrays with different shapes horizontally.
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
concatenated_horizontal = np.concatenate((arr1, arr2), axis=0)
print(concatenated_horizontal)

# 20. Function to vertically stack multiple NumPy arrays given as a list.
def vertical_stack(arr_list):
    return np.vstack(arr_list)

print(vertical_stack([np.array([1, 2, 4]), np.array([5, 6, 8])]))

# 21. Function to create an array of integers within a range with a step size.
def range_with_step(start, stop, step):
    return np.arange(start, stop + + step, step)

print("Range with step:", range_with_step(1, 10, 2))

# 22. Function to generate an array of 10 equally spaced values between 0 and 1.
def generate_equally_spaced():
    return np.linspace(0, 1, 10)

print("Equally spaced values:", generate_equally_spaced())

# 23. Function to create an array of 5 logarithmically spaced values between 1 and 1000.
def generate_log_space():
    return np.logspace(0, 3, 5)

print("Logarithmically spaced values:", generate_log_space())

# 24. Create a Pandas DataFrame with random integers between 1 and 100.
random_data = np.random.randint(1, 101, size=(5, 3))
df = pd.DataFrame(random_data, columns=['A', 'B', 'C'])

print(df)

# 25. Function to replace negative values in a specific column with zeros.
def replace_negatives_with_zeros(df, column_name):
    df[column_name] = np.where(df[column_name] < 0, 0, df[column_name])
    return df

df['A'] = [-10, 20, 30, -40, 50]  # Modify column 'A' for testing
print("DataFrame before replacing negatives:\n", df)

# 26. Access the 3rd element from a given NumPy array.
arr = np.array([10, 20, 30, 40, 50])
third_element = arr[2]
print(third_element)

# 27. Retrieve the element at index (1, 2) from a 2D NumPy array.
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
element_at_1_2 = arr_2d[1, 2]
print(element_at_1_2)

# 28. Extract elements greater than 5 using boolean indexing.
arr = np.array([3, 8, 2, 10, 5, 7])
greater_than_5 = arr[arr > 5]
print(greater_than_5)

# 29. Perform slicing to extract elements from index 2 to 5 (inclusive).
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
sliced_array = arr[2:6]
print(sliced_array)

# 30. Slice a 2D NumPy array to extract a sub-array `[[2, 3], [5, 6]]`.
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
sub_array = arr_2d[0:2, 1:3]
print(sub_array)

# 31. Extract elements in specific order based on indices in another array.
def extract_elements(arr, indices):
    return arr[tuple(indices.T)]

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

indices = np.array([[0, 1],  # Element at (0, 1) => 2
                    [2, 2],  # Element at (2, 2) => 9
                    [1, 0]]) # Element at (1, 0) => 4

print("Extracted elements:", extract_elements(arr, indices))

# 32. Filter elements greater than a threshold using boolean indexing.
def filter_greater_than(arr, threshold):
    return arr[arr > threshold]

arr = np.array([1, 2, 3, 4, 5])
print(filter_greater_than(arr, 3))

# 33. Extract specific elements from a 3D array using indices for each dimension.
def extract_from_3d(arr, x_indices, y_indices, z_indices):
    return arr[x_indices, y_indices, z_indices]

arr_3d = np.arange(27).reshape(3, 3, 3)
x_indices = [0, 1, 2]
y_indices = [1, 1, 1]
z_indices = [2, 0, 1]
print(extract_from_3d(arr_3d, x_indices, y_indices, z_indices))

# 34. Return elements satisfying two conditions using boolean indexing.
def elements_satisfying_conditions(arr, cond1, cond2):
    return arr[(cond1) & (cond2)]

arr = np.array([1, 2, 3, 4, 5, 6])
print(elements_satisfying_conditions(arr, arr > 2, arr < 5))

# 35. Extract elements using row and column indices.
def extract_using_indices(arr, row_indices, col_indices):
    return arr[row_indices, col_indices]

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rows = [0, 1, 2]
cols = [2, 1, 0]
print(extract_using_indices(arr, rows, cols))

# 36. Add a scalar value using broadcasting.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr + 5)

# 37. Multiply rows of arr2 by corresponding elements in arr1 using broadcasting.
arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr2 * arr1.T)

# 38. Add arr1 to each row of arr2 using broadcasting.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(arr2 + arr1[:, np.newaxis])

# 39. Add arrays using broadcasting.
arr1 = np.array([[1], [2], [3]])
arr2 = np.array([[4, 5, 6]])
print(arr1 + arr2)

# 40. Handle shape incompatibility for multiplication.
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8], [9, 10]])
try:
    print(arr1 * arr2)
except ValueError as e:
    print(f"Error: {e}")

# 41. Calculate column-wise mean.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.mean(axis=0))

# 42. Find maximum value in each row.
print(arr.max(axis=1))

# 43. Indices of maximum value in each column.
print(arr.argmax(axis=0))

# 44. Calculate moving sum along rows.
def moving_sum(arr, window_size=2):
    return np.array([np.convolve(row, np.ones(window_size, dtype=int), mode='valid') for row in arr])

print(moving_sum(arr))

# 45. Check if all elements in each column are even.
print((arr % 2 == 0).all(axis=0))

# 46. Reshape an array into a matrix of dimensions m x n.
def reshape_array(arr, m, n):
    return arr.reshape(m, n)

# Example:
original_array = np.array([1, 2, 3, 4, 5, 6])
print(reshape_array(original_array, 2, 3))

# 47. Flatten a matrix into an array.
def flatten_matrix(matrix):
    return matrix.flatten()

# Example:
input_matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(flatten_matrix(input_matrix))

# 48. Concatenate two arrays along a specified axis.
def concatenate_arrays(arr1, arr2, axis):
    return np.concatenate((arr1, arr2), axis=axis)

# Example:
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
print(concatenate_arrays(array1, array2, axis=0))

# 49. Split an array into multiple sub-arrays along a specified axis.
def split_array(arr, indices, axis):
    return np.split(arr, indices, axis=axis)

# Example:
original_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(split_array(original_array, [1], axis=0))

# 50. Insert and delete elements at specified indices.
def insert_and_delete(arr, insert_indices, insert_values, delete_indices):
    arr = np.insert(arr, insert_indices, insert_values)
    arr = np.delete(arr, delete_indices)
    return arr

# Example:
original_array = np.array([1, 2, 3, 4, 5])
indices_to_insert = [2, 4]
values_to_insert = [10, 11]
indices_to_delete = [1, 3]
print(insert_and_delete(original_array, indices_to_insert, values_to_insert, indices_to_delete))

# 51. Element-wise addition between random integers and a fixed array.
arr1 = np.random.randint(1, 10, size=5)
arr2 = np.arange(1, 6)
print(arr1 + arr2)

# 52. Element-wise subtraction.
arr1 = np.arange(10, 0, -1)
arr2 = np.arange(1, 11)
print(arr1 - arr2)

# 53. Element-wise multiplication.
arr1 = np.random.randint(1, 10, size=5)
arr2 = np.arange(1, 6)
print(arr1 * arr2)

# 54. Element-wise division.
arr1 = np.arange(2, 11, 2)
arr2 = np.arange(1, 6)
print(arr1 / arr2)

# 55. Element-wise exponentiation.
arr1 = np.arange(1, 6)
arr2 = arr1[::-1]
print(arr1 ** arr2)

# 56. Count occurrences of a substring in an array of strings.
def count_substring(arr, substring):
    return np.char.count(arr, substring)

# Example:
arr = np.array(['hello', 'world', 'hello', 'numpy', 'hello'])
print(count_substring(arr, 'hello'))

# 57. Extract uppercase characters from an array of strings.
def extract_uppercase(arr):
    return [''.join(filter(str.isupper, s)) for s in arr]

# Example:
arr = np.array(['Hello', 'World', 'OpenAI', 'GPT'])
print(extract_uppercase(arr))

# 58. Replace occurrences of a substring in a NumPy array of strings with a new string.
def replace_substring(arr, old_substring, new_substring):
    return np.char.replace(arr, old_substring, new_substring)

# Example:
arr = np.array(['apple', 'banana', 'grape', 'pineapple'])
print(replace_substring(arr, 'apple', 'orange'))

# 59. Concatenate strings in a NumPy array element-wise.
def concatenate_strings(arr):
    return ''.join(arr)

# Example:
arr = np.array(['Hello', ' ', 'World'])
print(concatenate_strings(arr))

# 60. Find the length of the longest string in a NumPy array.
def longest_string_length(arr):
    return max(np.char.str_len(arr))

    # Example:
arr = np.array(['apple', 'banana', 'grape', 'pineapple'])
print(longest_string_length(arr))

# 61. Create a dataset of 100 random integers between 1 and 1000 and compute statistical measures.
dataset = np.random.randint(1, 1001, size=100)
mean = np.mean(dataset)
median = np.median(dataset)
variance = np.var(dataset)
std_dev = np.std(dataset)
print(f"Mean: {mean}, Median: {median}, Variance: {variance}, Standard Deviation: {std_dev}")

# 62. Find the 25th and 75th percentiles of an array of 50 random numbers.
random_numbers = np.random.randint(1, 101, size=50)
percentile_25 = np.percentile(random_numbers, 25)
percentile_75 = np.percentile(random_numbers, 75)
print(f"25th Percentile: {percentile_25}, 75th Percentile: {percentile_75}")

# 63. Compute the correlation coefficient between two arrays.
arr1 = np.random.rand(100)
arr2 = np.random.rand(100)
correlation_coefficient = np.corrcoef(arr1, arr2)[0, 1]
print(f"Correlation Coefficient: {correlation_coefficient}")

# 64. Perform matrix multiplication using NumPy's dot function.
matrix1 = np.random.randint(1, 10, size=(3, 3))
matrix2 = np.random.randint(1, 10, size=(3, 3))
matrix_multiplication = np.dot(matrix1, matrix2)
print(f"Matrix Multiplication:\n{matrix_multiplication}")

# 65. Calculate the 10th, 50th (median), and 90th percentiles, and first and third quartiles of an array.
arr = np.random.randint(10, 1001, size=50)
percentile_10 = np.percentile(arr, 10)
percentile_50 = np.percentile(arr, 50)
percentile_90 = np.percentile(arr, 90)
first_quartile = np.percentile(arr, 25)
third_quartile = np.percentile(arr, 75)
print(f"10th Percentile: {percentile_10}, 50th Percentile (Median): {percentile_50}, 90th Percentile: {percentile_90}")
print(f"First Quartile: {first_quartile}, Third Quartile: {third_quartile}")

# 66. Find the index of a specific element in an array.
arr = np.array([10, 20, 30, 40, 50])
index_of_30 = np.where(arr == 30)[0][0]  # Using where to find the index of 30
print(f"Index of 30: {index_of_30}")

# 67. Sort a random array in ascending order.
random_array = np.random.randint(1, 101, size=10)
sorted_array = np.sort(random_array)
print(f"Sorted Array: {sorted_array}")

# 68. Filter elements >20 in the given array.
arr = np.array([12, 25, 6, 42, 8, 30])
filtered_arr = arr[arr > 20]
print(f"Filtered elements > 20: {filtered_arr}")

# 69. Filter elements divisible by 3.
arr = np.array([1, 5, 8, 12, 15])
filtered_arr = arr[arr % 3 == 0]
print(f"Filtered elements divisible by 3: {filtered_arr}")

# 70. Filter elements which are ≥ 20 and ≤ 40.
arr = np.array([10, 20, 30, 40, 50])
filtered_arr = arr[(arr >= 20) & (arr <= 40)]
print(f"Filtered elements ≥ 20 and ≤ 40: {filtered_arr}")

# 71. Check the byte order of an array using dtype's byteorder attribute.
arr = np.array([1, 2, 3])
byte_order = arr.dtype.byteorder
print(f"Byte Order: {byte_order}")

# 72. Perform byte swapping in place using `byteswap()`.
arr = np.array([1, 2, 3], dtype=np.int32)
arr.byteswap(inplace=True)
print(f"Byte-swapped array (in place): {arr}")

# 73. Swap the byte order without modifying the original array using `newbyteorder()`.
arr = np.array([1, 2, 3], dtype=np.int32)
new_arr = arr.newbyteorder()
print(f"Original Array: {arr}, Swapped Array: {new_arr}")

# 74. Swap byte order conditionally based on system endianness using `newbyteorder()`.
arr = np.array([1, 2, 3], dtype=np.int32)
if arr.dtype.byteorder == '=':  # Check if system's native byte order
    swapped_arr = arr.newbyteorder()
    print(f"Conditionally byte-swapped array: {swapped_arr}")

# 75. Check if byte swapping is necessary for the current system using `dtype` attribute `byteorder`.
byte_order = arr.dtype.byteorder
if byte_order in ('>', '<'):
    print(f"Byte swapping necessary, byte order: {byte_order}")
else:
    print(f"No byte swapping needed, byte order: {byte_order}")

# 76. Create `arr1`, copy it, modify the copy, and check for independence.
arr1 = np.arange(1, 11)
copy_arr = arr1.copy()
copy_arr[0] = 99
print(f"Original Array: {arr1}, Copied Array: {copy_arr}")

# 77. Extract a slice from a matrix, modify it, and check if the matrix changes.
matrix = np.random.randint(1, 10, size=(3, 3))
view_slice = matrix[1:, 1:]
view_slice[0, 0] = 99
print(f"Modified Slice: {view_slice}, Original Matrix: {matrix}")

# 78. Broadcast addition on a slice and check for changes in the original array.
array_a = np.arange(1, 13).reshape(4, 3)
view_b = array_a[1:, 1:]
view_b += 5
print(f"Modified Slice: {view_b}, Original Array: {array_a}")

# 79. Create a reshaped view and modify it to check if the original array reflects changes.
orig_array = np.arange(1, 9).reshape(2, 4)
reshaped_view = orig_array.reshape(4, 2)
reshaped_view[0, 0] = 99
print(f"Reshaped View: {reshaped_view}, Original Array: {orig_array}")

# 80. Extract a copy of elements > 5, modify the copy, and verify the original remains unchanged.
data = np.random.randint(1, 10, size=(3, 4))
data_copy = data[data > 5].copy()
data_copy[0] = 99
print(f"Data Copy: {data_copy}, Original Data: {data}")

# 81. Perform addition and subtraction on two matrices of identical shape.
A = np.random.randint(1, 10, size=(2, 3))
B = np.random.randint(1, 10, size=(2, 3))
print(f"Addition: {A + B}, Subtraction: {A - B}")

# 82. Perform matrix multiplication between two matrices of compatible dimensions.
C = np.random.randint(1, 10, size=(3, 2))
D = np.random.randint(1, 10, size=(2, 4))
matrix_product = np.dot(C, D)
print(f"Matrix Multiplication:\n{matrix_product}")

# 83. Find the transpose of a matrix.
E = np.random.randint(1, 10, size=(2, 3))
transpose_E = E.T
print(f"Original Matrix:\n{E}, Transpose:\n{transpose_E}")

# 84. Compute the determinant of a square matrix.
F = np.random.randint(1, 10, size=(3, 3))
determinant_F = np.linalg.det(F)
print(f"Square Matrix:\n{F}, Determinant: {determinant_F}")

# 85. Find the inverse of a square matrix.
G = np.random.randint(1, 10, size=(3, 3))
if np.linalg.det(G) != 0:  # Ensure the matrix is invertible
    inverse_G = np.linalg.inv(G)
    print(f"Original Matrix:\n{G}, Inverse:\n{inverse_G}")
else:
    print("Matrix is singular and not invertible.")