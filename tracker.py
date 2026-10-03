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

subtotal = 0

item1 = input("First expenses? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expenses? ")
amount2 = float(input("Amount? "))
subtotal += amount2

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * tax_percent / 100
total = subtotal + tax

budget = float (input("Your budget? "))
over_budget = total > budget
left = budget - total


print("\n--------------------------------------")
print("SUMMARY")
print(f"\t- {item1}:\t${amount1}")
print(f"\t- {item2}:\t${amount2}")
print(f"Subtotal:\t\t${subtotal}")
print(f"Average:\t\t${average}")
print(f"Tax ({tax_percent}%):\t\t${tax}")
print(f"Grand total:\t\t${total}")
print(f"Over budget?:\t\t${over_budget}")
print(f"Left in budget:\t\t${left}")
print("-------------------------------------------")
print("Made by: Julian A. Magrata | Installment 1")
