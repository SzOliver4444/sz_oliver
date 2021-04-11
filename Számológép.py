print("Számológép")
        
def add(x,y):
	return x + y
def substract(x,y):
	return x - y
def multiply(x,y):
	return x * y
def divide(x,y):
	return x/y

print("Válassz műveletet")
print("1. Összeadás")
print("2. Kivonás")
print("3. Szorzás")
print("4. Osztás")
choice = input("Választott művelet (1/2/3/4): ")

num1=int(input("Első szám: "))
num2=int(input("Második szám: "))

if choice == '1' :
	print(num1, "+", num2, "=", add(num1,num2))
elif choice == '2' :
	print(num1, "-", num2, "=", substract(num1,num2))
elif choice == '3' :
	print(num1, "x", num2, "=", multiply(num1,num2))
elif choice == '4' :
	print(num1, "/", num2, "=", divide(num1,num2))
else:
	print("Invalid input")
