#৩- ফাংশন ব্যবহার করে কোন সংখ্যার ফ্যাক্টরিয়াল মান নির্ণয়ের  প্রোগ্রাম।
#3- Program to determine the factorial value of a number using functions.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("input a number to compute the factorial: "))
print(factorial(n))
