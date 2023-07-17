def evaluate_polynomial(coefficients,n):
  result = 0
  for i in range(len(coefficients)):
   result += coefficients[i] * (n**i)
   return result
 
coefficients=[9,2,4]
n=5
evaluate_polynomial(coefficients,n)
print(f"The value of polynomial f({n}) is {evaluate_polynomial(coefficients,n)}")