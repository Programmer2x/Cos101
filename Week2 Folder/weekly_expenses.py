#Input
name=input("Student Name: ")
daily_trans=float(input("Daily Transport Cost: "))
daily_feed=float(input("Daily Feeding Cost: "))
days=int(input("Days on campus: "))
other_exp=float(input("Other Weekly Expenses: "))

#Process
trans_tot=daily_trans*days
feed_tot=daily_feed*days
week_tot=trans_tot+feed_tot+other_exp

#Output
print()
print("\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("Weekly Expense Summary:")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\")
print()
print(f"Student:{name}")
print("Transport Total:",format(trans_tot,".2f"))
print("Feeding Total:",format(feed_tot,".2f"))
print("Other Expenses:",format(other_exp,".2f"))
print("Weekly Total:",format(week_tot,".2f"))










