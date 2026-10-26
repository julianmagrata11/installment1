# Julian A. Magrata
#Installment 4
print("========================================")
print("\t\tEXPENSIVE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)
print("\nWelcome! This is your personal expense tracker.\n")
print("MAIN MENU")
print("\t1) Add an expenses\t(coming soon)")
print("\t2) View all expenses\t(coming soon)")
print("\t3) Show total spent\t(coming soon)")
print("\t4) Exit\t\t\t(coming soon)")

name = input("\nWhat's your name?")
print (f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("First expenses? ")
amount1 = float(input("Amount? "))
subtotal += amount1

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("Second expenses? ")
amount2 = float(input("Amount? "))
subtotal += amount2

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")
    
if amount1 > 100 and amount2 > 100:
    print("Two big expenses in a row - slow down!")
    
    
    
average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * tax_percent / 100
total = subtotal + tax

budget = float(input("Your budget? "))  

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

if over_budget:
    print(f"Over budget by ${total - budget}!")
elif total > budget * 0.90:
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")
print("-------------------------------------------")
print("Made by: Julian A. Magrata | Installment 4")
