days_in_month = {
    1: 31,  # jan
    2: 28,  # feb
    3: 31,  # mar
    4: 30,  # apr
    5: 31,  # may
    6: 30,  # jun
    7: 31,  # jul
    8: 31,  # aug
    9: 30,  # sep
    10: 31, # oct
    11: 30, # nov
    12: 31  # dec
}

month = int(input("Enter month number (1-12): "))

if month in days_in_month:
    print("That month has", days_in_month[month], "days")
else:
    print("Uh oh! That month does not exist!")