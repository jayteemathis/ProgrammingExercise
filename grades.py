import csv  #import the csv module for reading and writing CSV files

def create_grades_file():
    """
    This function collects student names and three exam grades
    and writes them to a CSV file named grades.csv.
    """
    #askthe instructor how many students they want to enter
    num_students = int(input("How many students do you want to enter? "))

    #open grades.csv in write mode using 'with' to handle the file safely
    with open('grades.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        #write the header row to the CSV file
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        #loop for each student to collect their data
        for i in range(num_students):
            print(f"\nEntering info for student #{i + 1}:")
            first_name = input("First name: ")  # Get first name as string
            last_name = input("Last name: ")    # Get last name as string

            #gett three exam grades as integers
            exam1 = int(input("Exam 1 grade: "))
            exam2 = int(input("Exam 2 grade: "))
            exam3 = int(input("Exam 3 grade: "))

            #write this student's data as a new row in the CSV
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\nData has been saved to grades.csv.")


def display_grades_file():
    """
    This function reads the grades.csv file
    and displays its contents in a neatly formatted table.
    """
    #open grades.csv in read mode using 'with'
    with open('grades.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)

        #read the first row (header) from the file
        header = next(reader)

        print("\nStudent Grades")
        print("-" * 60)

        #print the header row with column spacing
        print(f"{header[0]:<15}{header[1]:<15}{header[2]:<10}{header[3]:<10}{header[4]:<10}")
        print("-" * 60)

        #print each student record in the same format
        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")

        print("-" * 60)


