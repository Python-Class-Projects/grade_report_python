'''
Write a program that reads from a file. The program will run through the file and fetch data seperating with a "tab" delimiter. The program will determine the semester, hours,
points, gpa and standing by reading the file. Then the program will calculate the cumulative values. Once everything is calculated, a screen outputting the data will
be surrounded by dashes to indicate a border around the results as shown in the homework.   
'''

#function to welcome the user to the program.
def welcome_message(amount):
	report_string = "Grade Report Tool"
	print("\n")
	print("*"*amount)
	print(report_string.center(amount))
	print("*"*amount)
	print("\n")

#function for the top outline portion of the border around the results, as well as displaying the title columns for the border. 
def top_outline(amount):
	print("{0:<15} {1:^10} {2:^10} {3:^10} {4:^10}".format("Semester","Hours","Points","GPA","Standing"))
	print("-"*amount)

#function for the bottom outline portion of the border around the results, as well as displaying the cumulative results for the row section.
def bottom_outline(amount):
	print("-"*amount)

#function to determine if the student made honors or not as well as determining if the student made the deans list.
def made_deans_list(gpa):
	if gpa >= 3.5:
		deans_list = "DEAN'S LIST"
		honors = "HONORS"
	return deans_list,honors

welcome_message(60)

#Where program starts, asking user for file name and opening file.
file = input("Enter name of grade report file: ")
print("\nHere is your grade summary:\n")

myfile = open(file, "r")

#Variable initialization
semester_title = ""
semester_hour = 0
semester_hours = 0
semester_grade = 0
semester_points = 0 
cumulative_semester_points = 0
cumulative_points = 0
cumulative_hours = 0
gpa = 0
cumulative_gpa = 0
deans_list = ""


top_outline(60)

#Reading the file with a for loop and stripping the line of any white space. 
for line in myfile:
	line = line.strip()

	parts = line.split("\t") #parts will contain the data for which the program will read, store and store values for which to add during the program.

	#if line == "" will print out the results for each semester as each semester is followed by an empty string to end the semester. Perfect time to print.
	if line == "":
		gpa = semester_points / semester_hours
		if gpa >= 3.5:
			deans_list = "DEAN'S LIST"
		print(f"{semester_title:<15} {semester_hours:^10} {semester_points:^10.2f} {gpa:^10.2f} {deans_list:^10}")

	#if parts contains 2 elements, we know that it is time to restart the values as it is a new semester.	
	elif len(parts) == 2:
		semester_title = parts[1]
		semester_points = 0
		semester_hours = 0
	#if parts contains 4 elements, we understand that we need to use the data here and store it inside variables.
	elif len(parts) == 4:
		semester_hour = float(parts[2]) #need to make hour into a float data type to be able to multiply with the other float numbers. 
		semester_hours += int(semester_hour) #need to make into int to remove to decimal places.
		cumulative_hours += int(semester_hour) #need to make into int to remove to decimal places.
		semester_grade = parts[3]

		#We are obtaining the points for the letter grade quality points * credit hours 
		points = 0
		if semester_grade == "A":
			points = semester_hour * 4.0 
			semester_points += points
			cumulative_points += points

		elif semester_grade == "B+":
			points = semester_hour * 3.3
			semester_points += points
			cumulative_points += points

		elif semester_grade == "B":
			points = semester_hour * 3.0
			semester_points += points
			cumulative_points += points

		elif semester_grade == "B-":
			points = semester_hour * 2.7
			semester_points += points
			cumulative_points += points

#Because the file does not read the last empty string, we must specify the remaining code here. 
gpa = semester_points / semester_hours
deans_list, honors = made_deans_list(gpa) #Obtaining if student made deans list and honors from the made_deans_list function with parameter of (gpa)

print(f"{semester_title:<15} {semester_hours:^10} {semester_points:^10.2f} {gpa:^10.2f} {deans_list:^10}") #printing the remaining results that did not get read because of empty string.
bottom_outline(60)

cumulative_gpa = cumulative_points / cumulative_hours #calculating cumulative gpa
print("{0:<15} {1:^10} {2:^10.2f} {3:^10.2f} {4:^10}".format("Cumulative",cumulative_hours,cumulative_points,cumulative_gpa,honors)) #printing the last row
print("\nEND OF PROGRAM")

myfile.close()
