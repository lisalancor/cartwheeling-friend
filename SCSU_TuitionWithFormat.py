# Working with nice formatting in Python 3.5
# Program Written by:  Lisa Lancor
# For Demo in CSC 152 - Fall 2016

# Calculate the In-State Total for Undergraduate Students at SCSU

fall_tuition = 2608
fall_univ_general_fee = 1902
fall_univ_fee = 432
fall_activity_fee = 70
fall_media_fee = 15

fall_total = fall_tuition + fall_univ_general_fee \
             + fall_univ_fee + fall_activity_fee \
             + fall_media_fee

print("\n\nIn-State \t\t Undergraduate")
print("---------------------------------------")
print("Tuition", format(fall_tuition, '25,d'))
print("University General Fee", format(fall_univ_general_fee, '10,d'))
print("University  Fee", format(fall_univ_fee, '17,d'))
print("Student Activity Fee", format(fall_activity_fee, '12,d'))
print("Media Fee", format(fall_media_fee, '23,d'))
print("---------------------------------------")
#print("Term Total", format(fall_total, '22,d'))
# Want final term total with a $ indicating payment in dollars
# Need to use tabs \t\t
print("Term Total \t\t   $", format(fall_total, ',.2f'), sep='')

# Now calculate 6.35% CT Sales tax on the Term Total. 
total_tax = fall_total * 0.0635
print("CT Sales Tax", format(total_tax, '23,.2f'))
print("---------------------------------------")
print("Overall Total \t\t   $", format(fall_total+total_tax, ',.2f'), sep='')

print("\n\n")
