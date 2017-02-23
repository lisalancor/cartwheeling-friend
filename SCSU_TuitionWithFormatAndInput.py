# Working with nice formatting in Python 3.5
# Program Written by:  Lisa Lancor
# For Demo in CSC 152 - Fall 2016

# Calculate the In-State Total for Undergraduate Students at SCSU

fall_total = float(input("Enter the Term Total for Fall: "))

fall_tuition = 0.5188 * fall_total
fall_univ_general_fee = 0.3784 * fall_total
fall_univ_fee = 0.086 * fall_total
fall_activity_fee = 0.0139 * fall_total
fall_media_fee = 0.003 * fall_total

print("\n\nIn-State \t\t Undergraduate")
print("---------------------------------------")
print("Tuition", format(fall_tuition, '25,.0f'))
print("University General Fee", format(fall_univ_general_fee, '10,.0f'))
print("University  Fee", format(fall_univ_fee, '17,.0f'))
print("Student Activity Fee", format(fall_activity_fee, '12,.0f'))
print("Media Fee", format(fall_media_fee, '23,.0f'))
print("---------------------------------------")
# Want final term total with a $ indicating payment in dollars
# Need to use tabs \t\t
print("Term Total \t\t   $", format(fall_total, ',.2f'), sep='')

# Now calculate 6.35% CT Sales tax on the Term Total. 
total_tax = fall_total * 0.0635
print("CT Sales Tax", format(total_tax, '23,.2f'))
print("---------------------------------------")
print("Overall Total \t\t   $", format(fall_total+total_tax, ',.2f'), sep='')

print("\n\n")
