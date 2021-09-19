# confirm which months constituted the current term


def validate_entry():
    lst = []
    while True:
        test_user_input = input("How many test scores would you like to sum?\n:")
        if not test_user_input.isdigit():  # "if not" means if user input is not a digit
            print("Invalid entry!")
        else:
            test_user_entry = int(test_user_input)

            for n in range(test_user_entry):
                while True:
                    test_samples = input("Please enter your test score:\n")
                    if not test_samples.isdigit():
                        print("This is not a valid entry!")
                    else:
                        test_score = int(test_samples)
                        if test_score <= 10:
                            lst.append(test_score)
                            break
                        print("test score cannot be greater than 10!")

            return f"{sum(lst)}"


user_test = validate_entry()
print(user_test)


def exam_user_score():
    while True:
        user_exam = input("What is the exam score?\n")
        if not user_exam.isdigit():
            print("Your entry is not a digit!")
        else:
            exam_score = int(user_exam)
            if exam_score <= 70:
                total_exam_test = exam_score
                return f"{total_exam_test}"
            else:
                print("Exam score cannot be more than 70")


final_exam = exam_user_score()
print(final_exam)


def test_exam(test, exam):
    total_test_exam = int(test) + int(exam)
    return f"The test and exam total is {total_test_exam}"


test_exam_final = test_exam(user_test, final_exam)
print(test_exam_final)


def months_in_terms():
    what_term = input("what term's examination did you just record?\n")
    num_of_months = input(f"what are the months in {what_term}?\n")
    month = num_of_months.split(", ")
    print(type(month))
    print(month[1])
    confirm = input(
        f'Are you saying you recorded {what_term}"s examinations and that the '
        f'months in {what_term} are {num_of_months}?\n').lower()
    if confirm != 'yes':  # how to make input either uppercase or lowercase?
        print("Please correct the error!")
    else:
        print('Noted!')


months_in_terms()

terminate_cmd = ""
while terminate_cmd != "stop":
    terminate_cmd = input("Kindly exit the program!\n")