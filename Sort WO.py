import os
import shutil

paste_wo = """1231313
1231312
1231312
1231315
1231314
"""

paste_sb = """111111
222222
333333
444444
555555
"""

Wo_numbers_unique = []


def unique_Wo_numbers_list(nums):
    global Wo_numbers_unique
    list_of_numbers = nums
    lines = list_of_numbers.splitlines()
    numbers = [int(line) for line in lines]

    unique_numbers = set(numbers)
    new_list_of_numbers = list(unique_numbers)
    Wo_numbers_unique = new_list_of_numbers

    return numbers


Sb_no = unique_Wo_numbers_list(paste_sb)
Wo_no = unique_Wo_numbers_list(paste_wo)

print(Sb_no, Wo_no, Wo_numbers_unique)


def view_files_from_path():
    # Get the list of all files in the directory.
    files = os.listdir(path)

    # Filter the list to only include PDF files.
    pdf_files = [file for file in files if file.endswith(".pdf")]

    # Print the list of PDF files.
    return pdf_files


def make_folders():
    for i in Wo_numbers_unique:
        os.mkdir(Wo_path + "\\" + str(i))


def validate_input(sb_number):
    for i in pdfs:
        if i[0:len(sb_number)] == sb_number:
            return True
    else:
        return False


path = ''
Wo_path = ''
# pdfs = view_files_from_path()


def validate_input(Sb):
    a = Sb[0:7]
    for i in range(0, len(Sb_no)):
        if a == str(Sb_no[i]):
            return i
    return -1


def main():
    error_log = ""
    for i in pdfs:
        a = validate_input(i)
        if a == -1:
            error_log += i + "  Kindly check this file\n"
        else:
            src = path + "\\" + i
            dest = Wo_path + "\\" + str(Wo_no[a])
            shutil.copy(src, dest)

    if error_log != "":
        # Open the text file in write mode
        with open("error_log.txt", "w") as f:
            # Write the string to the file
            f.write(error_log)

        # Close the file
        f.close()
        print("Error file has been generated Please check!!")


# make_folders()
# main()
