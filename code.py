#!/usr/bin/env python

import sys

def after(date: str) -> str:
    "Returns the next date in the same format."
    if len(date) != 10:  
        return '0000-00-00'  
    else:
        str_year, str_month, str_day = date.split('-') 
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        lyear = year % 4  
        if lyear == 0:
            feb_max = 29 
        else:
            feb_max = 28 

        lyear = year % 100
        if lyear == 0:       
            feb_max = 28

        lyear = year % 400
        if lyear == 0:
            feb_max = 29

        tmp_day = day + 1 

        mon_max = {1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if tmp_day > mon_max[month]:
            to_day = tmp_day % mon_max[month] 
            tmp_month = month + 1
            if tmp_month > 12:
                tmp_month = 1
                year = year + 1
        else:
            to_day = tmp_day
            tmp_month = month

        next_date = f"{year}-{tmp_month:02}-{to_day:02}"
        return next_date

def before(date: str) -> str:
    "Returns the previous date in the same format."
    if len(date) != 10:  
        return '0000-00-00'   
    else:
        str_year, str_month, str_day = date.split('-') 
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        lyear = year % 4  
        if lyear == 0:
            feb_max = 29 
        else:
            feb_max = 28

        lyear = year % 100
        if lyear == 0:       
            feb_max = 28

        lyear = year % 400
        if lyear == 0:
            feb_max = 29

        tmp_day = day - 1   

        mon_max = {1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if tmp_day < 1:     
            month = month - 1
            if month < 1:
                month = 12
                year = year - 1
            to_day = mon_max[month]     
        else:
            to_day = tmp_day

        previous_date = f"{year}-{month:02}-{to_day:02}"
        return previous_date 

if __name__ == "__main__":
    while True:
        print("1. After date")
        print("2. Before date")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date in YYYY-MM-DD format: ")
            print(after(date))
        elif choice == '2':
            date = input("Enter the date in YYYY-MM-DD format: ")
            print(before(date))
        elif choice == '3':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please choose again.")

