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


terminate_cmd = ""
while terminate_cmd != "stop":
    terminate_cmd = input("Kindly exit the program!\n")

# def num_of_m():
#     #months_one = [(input("input the number of months\n")).split(", ")]
#     months_one = input ("input the number of months\n",).split(", ")# input("input the next\n").split(", ")
#
#     #num = [months_one]
#     #month_list = input("input the number of months\n")
#     #months_one = month_list.split(", ")
#     #for months in set(month_list):
#     print(type{(months_one)})
#     print({months_one})
#     #print(months_one.index(1))
#
# num_of_m()
