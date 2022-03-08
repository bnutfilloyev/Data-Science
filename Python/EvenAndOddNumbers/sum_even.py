#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
#Create a variable "sum_even" and assign it 0.
#Find the sum of the even digits in the variable "var_int".

var_int = 1234
sum_even = 0

first = ((var_int // 1000) + 1) % 2
second = ((var_int // 100) + 1) % 2
third = ((var_int // 10) + 1) % 2
fourth = (var_int + 1) % 2

print(first + second + third + fourth)