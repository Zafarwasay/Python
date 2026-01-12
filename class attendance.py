def check_attendance_eligibility():
    try:
        
        total_classes = int(input("Enter total number of classes held: "))
        attended_classes = int(input("Enter number of classes attended: "))


        attendance_percentage = (attended_classes / total_classes) * 100
        print(f"Your attendance is: {attendance_percentage:.2f}%")

        
        if attendance_percentage >= 75:
            print("Status: ELIGIBLE for the exam.")
        else:
            print("Status: NOT ELIGIBLE. Minimum 75% attendance required.")
            
    except ZeroDivisionError:
        print("Error: Total classes cannot be zero.")
    except ValueError:
        print("Error: Please enter valid numerical values.")

check_attendance_eligibility()
