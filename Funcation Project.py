
# ------------------- FUNCTIONS -------------------

def calculator():
    print("\n***** Welcome to the Calculator *****")
    while True:
        print("\nSelect operator:")
        print("1. Addition\n2. Subtraction\n3. Division\n4. Multiply\n5. Exit Calculator")
        select = input("Select operator (1-5): ")

        if select == "5":
            print("Exiting Calculator...\n")
            break

        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))

        if select == "1":
            print(f"Result: {num1 + num2}")
        elif select == "2":
            print(f"Result: {num1 - num2}")
        elif select == "3":
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Cannot divide by zero!")
        elif select == "4":
            print(f"Result: {num1 * num2}")
        else:
            print("Wrong Input! Please select a valid operator.")

def student_marksheet():
    print("\n***** Student Marksheet *****")
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = {}
    subjects = ["Math", "Physics", "Chemistry", "English"]
    for subject in subjects:
        marks[subject] = float(input(f"Enter marks for {subject}: "))

    total = sum(marks.values())
    percentage = total / len(subjects)
    print(f"\nMarksheet for {name} (Roll No: {roll})")
    for subject, mark in marks.items():
        print(f"{subject}: {mark}")
    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage:.2f}%\n")

def cloting_store():
    print("\n***** Clothing Store *****")
    items = {"Shirt": 1500, "Jeans": 2500, "Jacket": 3500, "Shoes": 4000}
    print("Available items:")
    for item, price in items.items():
        print(f"{item}: Rs {price}")

    choice = input("Which item do you want to buy? ")
    if choice in items:
        print(f"You selected {choice}. Price: Rs {items[choice]}")
    else:
        print("Item not available.")

def car_recommendation():
    print("\n***** Car Recommendation System *****")
    budget = float(input("Enter your budget (in lakhs): "))
    if budget < 10:
        print("You can consider small cars like Suzuki Alto or Daihatsu Mira.")
    elif 10 <= budget < 30:
        print("You can consider sedans like Toyota Corolla or Honda City.")
    elif 30 <= budget < 50:
        print("You can consider SUVs like Toyota Fortuner or Honda CR-V.")
    else:
        print("You can consider luxury cars like BMW or Mercedes-Benz.")

# ------------------- MAIN APP -------------------

while True:
    print("Here are the available apps you can use:\n1. Calculator \n2. Student Marksheet \n3. Cloting Store \n4. Car Recommendation Sysytem \n5. Exit")
    app_select = input("\nSelect an app (1-5): ")

    if app_select == "1":
        calculator()
    elif app_select == "2":
        student_marksheet()
    elif app_select == "3":
        cloting_store()
    elif app_select == "4":
        car_recommendation()
    elif app_select == "5":
        print("Exiting App Player. Goodbye!")
        break
    else:
        print("Invalid Input! Please select a number between 1-5.")