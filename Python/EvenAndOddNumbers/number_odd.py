#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".


var_int = 1233

first = (var_int // 1000) % 2
second = (var_int // 100) % 2
third = (var_int // 10) % 2
fourth = var_int % 2
print(first + second + third + fourth)