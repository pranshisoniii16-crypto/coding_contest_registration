# Coding Contest Registration 2026

class Student:

    def __init__(self, name, college):
        self.name = name
        self.college = college

    def display(self):
        print("\nStudent Name :", self.name)
        print("College Name :", self.college)


events = ["Beginner Coding", "Intermediate Coding", "Advanced Coding"]

fees = {
    "Beginner Coding": 200,
    "Intermediate Coding": 300,
    "Advanced Coding": 500
}

slots = ("Morning", "Afternoon", "Evening")


def calculate_bill(event):
    return fees[event]


print("\n================================")
print("Coding Contest Registration System")

name = input("\nEnter Name : ")
college = input("Enter College Name : ")

obj = Student(name, college)

print("\nAvailable Events")

for i in range(len(events)):
    print(i + 1, ".", events[i])
print("\n Please Note : ENTER NUMBER ONLY...!")
choice = int(input("\nChoose Event : "))

selected_event = events[choice - 1]

print("\nAvailable Slots")

for i in range(len(slots)):
    print(i + 1, ".", slots[i])
print("\n Please Note : ENTER NUMBER ONLY...!")
slot_choice = int(input("\nChoose Slot : "))

selected_slot = slots[slot_choice - 1]

total = calculate_bill(selected_event)

print("\n------REGISTRATION FINAL DETAILS------")

obj.display()

print("Event :", selected_event)
print("Slot :", selected_slot)
print("Registration Fee : Rs.", total)

print("\nThank You For Registering :) !")