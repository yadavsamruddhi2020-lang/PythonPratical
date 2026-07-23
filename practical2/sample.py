# driver


status=str(input("enter the status:"))
if status=="married":
    print("driver is married")
else:
    gender=str(input("enter gender"))
    age=int(input("enter the age"))
    if gender=="male" and age>=30:
        print("driver is unmarried,male and above 30")
    elif gender=="female" and age>=25:
        print("driver is unmarried , female and above 25")
    else:
        print("invalid")