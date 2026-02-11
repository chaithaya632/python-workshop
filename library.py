library_members = {
    101: "Rahul",
    102: "Anita",
    103: "Suresh"
}

print(" Library Management System :")

roll_no = int(input("Enter Roll Number: "))
name = input("Enter Name: ")

if roll_no in library_members:
    print("User already exists in data.")
    print("Name:", library_members[roll_no])
    print("Roll No:", roll_no)
else:
    library_members[roll_no] = name
    print("User added successfully.")
    print("Name:", name)
    print("Roll No:", roll_no)

print("\nUpdated Data:", library_members)