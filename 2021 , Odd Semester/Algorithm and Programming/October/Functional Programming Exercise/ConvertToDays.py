def convertToDays():
    hours = int(input("Enter number of hours:"))
    minutes = int(input("Enter number of minutes:"))
    seconds = int(input("Enter number of seconds:"))


    def getDays():
        days = hours/24 + minutes/1440 + seconds/86400
        return round(days,4)
    getDays()





