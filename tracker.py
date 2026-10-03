# Julian A. Magrata
print("========================================")
print("\t\tEXPENSIVE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)
print("\nWelcome! This is your personal expense tracker.\n")
print("Main menu")
print("\t1) Add an expenses\t(coming soon)")
print("\t2) View all expenses\t(coming soon)")
print("\t3) Show total spent\t(coming soon)")
print("\t4) Exit\t\t(coming soon)")

name = input("\nWhat's your name?")
print (f"Welcome, {name}! Let's log two expenses.")

item1 = input("First expenses?")
amount1 = float(input("Amount? "))
item2 = input("Second expenses?")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print("\n--------------------------------------")
print("SUMMARY")
print(f"\t- {item1}:\t${amount1}")
print(f"\t- {item2}:\t${amount2}")
print(f"Total spent:\t\t${total}")
print(f"Average:\t\t${average}")
print("-------------------------------------------")
print("Made by: Julian A. Magrata | Installment 1")
