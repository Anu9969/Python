def evaluate_polynomial(coefficients,n):
    result = 0
    for i in range(len(coefficients)):
      result += coefficients[i] * (n**i)
    return result
 
coefficients=[9,2,4]
n=5
polynomial_value = evaluate_polynomial(coefficients, n)
print(f"The value of the polynomial function f({n}) is: {polynomial_value}")


# def evaluate_polynomial(coefficients, n):
#     result = 0
#     for i in range(len(coefficients)):
#         result += coefficients[i] * (n ** (len(coefficients) - 1 - i))
#     return result

# # Coefficients of the polynomial function: 4n^2 + 2n + 9
# coefficients = [4, 2, 9]
# n = 5
# polynomial_value = evaluate_polynomial(coefficients, n)
# print(f"The value of the polynomial function f({n}) is: {polynomial_value}")



# def evaluate_polynomial(coefficients, n):
#     result = 0
#     for i in range(len(coefficients)):
#         result += coefficients[i] * (n ** i)
#     return result

# # Coefficients of the polynomial function: 4n^2 + 2n + 9
# coefficients = [9, 2, 4]
# n = 5
# polynomial_value = evaluate_polynomial(coefficients, n)
# print(f"The value of the polynomial function f({n}) is: {polynomial_value}")
