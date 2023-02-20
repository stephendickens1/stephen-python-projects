class Reminder:

    def __init__(self, name):
        self.name = name
    
    def remind_me_to(self, task):
        return f"{self.name}! {task}!"

reminder = Reminder("Kay")

print (reminder.remind_me_to("Walk the dog"))