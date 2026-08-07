s1 = int(input("Enter marks in subject 1: "))
s2 = int(input("Enter marks in subject 2: "))
s3 = int(input("Enter marks in subject 3: "))

total_percentage = (s1 + s2 + s3) / 3

if s1 >= 40 and s2 >= 40 and s3 >= 40 and total_percentage >= 40:
    print("Pass")
else:
    print("Fail")