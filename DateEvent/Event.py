from datetime import datetime

class Event:
    def __init__(self, name = "", dob = ""):
        self.__name = name
        self.__dob = dob
        self.printFlag = False

    def checkDate(self):
        date_str = self.__dob
        format_str = '%d/%m/%Y'
        datetime_obj = datetime.strptime(date_str, format_str)
        month_number = int(datetime_obj.strftime('%m'))
        self.mName = datetime_obj.strftime('%b')
        self.date = datetime_obj.strftime("%d").strip("0")

        if(month_number%2 == 0):
            self.flag = 'even'
        else:
           self.flag = 'odd'
            
        if self.flag == 'even':
            print("You are offered with the Birthday Bash on {0} {1} of this year".format(self.mName, self.date))
            self.printFlag = True
        else:
            print("You are not offered with the Birthday Bash")
            self.printFlag = True
        
        return ''
