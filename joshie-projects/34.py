for i in range(3):
    def is_perfect(n):
        num = [i for i in range(1, n) if n % i == 0]
        if sum(num) == n:
            print(n ," is a perfect number")
        elif (n == 0) or (n < 0):
            print("Number should be positive")
        else:
            print(n,"is not a perfect number")

    is_perfect(int(input("enter number: ")))
print("The program is finished.")
 