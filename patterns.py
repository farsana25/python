# n=int(input('enter the number'))
# for i in range(n):
#     print('*',end='  ')


# n=int(input('enter the range'))
# for i in range(n):
#         for j in range(n):
#             print('%',end=' ')
#         print()


# n=int(input('enter the range'))
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# # Define the size of the square
# size = 5

# # Loop through rows
# for i in range(size):
#     # Print a row of stars
#     print('*' * size)


# n=int(input('enter the limit'))
# for i in range(n+1):
#     for j in range(i+2):
#         for k in range(j-1):
#          print('f',end=' ')
#     print()

# n=int(input('enter the limit'))
# for i in range(n+2):
#     for j in range(i+1):
#      print('#',end=' ')
#     print()

# n = 7
# for i in range(1, n + 1, 2):  # Increment by 2 for odd-numbered rows
#     spaces = (n - i) // 2
#     print(" " * 4 * spaces, end="")  # Print leading spaces
#     for j in range(1, i + 1):
#         print(f"{j:<4}", end="")  # Print numbers with uniform spacing
#     print()