def convertToDays():
    hours = int(input("Enter number of hours:"))
    minutes = int(input("Enter number of minutes:"))
    seconds = int(input("Enter number of seconds:"))

    def getDays(h,m,s):
        days = round((h / 24 + m / 1440 + s / 86400),4)
        return days
    newDays = getDays(hours,minutes,seconds)
    print("Total of days is: ",newDays)

convertToDays()

