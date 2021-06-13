from datetime import datetime, date
class Hall:
    def __init__(self, start_date, end_date, cost_per_day):
        self.start_date = start_date
        self.end_date = end_date
        self.cost_per_day = cost_per_day

    def cost(self, d):
        print("Total cost", d * self.cost_per_day)

    def no_days(self):
        if not isinstance(self.start_date, datetime):
            date_object1 = datetime.strptime(self.start_date, '%b %d %Y').date()
            do2 = datetime.strptime(self.end_date, '%b %d %Y').date()
        else:
            date_object1 = self.start_date
            do2 = self.end_date

        ans = (do2 - date_object1).days
        print("\nTotal number of days", ans)

        self.cost(ans)
