# Name: Sharyn Miyaji
# Date: 11/20/2023
# Course: CS361 Section 400
# Assignment: 9
# Description:  Microservice for my partner, James Hill.  This program tracks how much money a Poker Player has in a
#               bank account.  The Poker Player can deposit or withdraw money from their account.



import time

class PlayerAccount:

    def __init__(self):
        self._playerlist = {}


    def withdraw_money(self, name, amount):
        current_amount = self._playerlist[name]["Amount"]
        if amount <= current_amount:
            current_amount -= amount
            self._playerlist[name]["Amount"] = current_amount
        else:
            print("Insufficient amount")

    def deposit_money(self, name, amount):
        if name not in self._playerlist:
            self._playerlist[name] = {"Name": name,
                                      "Amount": 0}
        current_amount = self._playerlist[name]["Amount"]
        current_amount += amount
        self._playerlist[name]["Amount"] = current_amount

    def get_amount(self, name):
        current_amount = self._playerlist[name]["Amount"]
        return current_amount


account = PlayerAccount()
while True:
    input_file = open('bankcomms.txt', 'r')
    first_line = input_file.readline()
    second_line = input_file.readline()
    second_line_split = second_line.split(' ')
    if "request" in first_line:

        time.sleep(2)
        name = str(second_line_split[0])
        action = str(second_line_split[1])
        amount = float(second_line_split[2])

        if action == "deposit":
            account.deposit_money(name, amount)
            total_amount = account.get_amount(name)
        elif action == "retrieve":
            account.withdraw_money(name, amount)
            total_amount = account.get_amount(name)
        time.sleep(2)
        output_file = open('bankcomms.txt', 'w')
        output_file.write("Successfully received")
        output_file.close()

    time.sleep(10)




