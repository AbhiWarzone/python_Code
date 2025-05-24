class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def showTrainNo(self):
        print(f"Train Number is: {self.trainNo}")

    def getStatus(self):
        print("Train is running on time")

    def bookStatus(self, fro, to):
        print(f"Ticket is booked successfully from {fro} to {to}")

# Create an instance of Train
t = Train(12345)

# Call the methods correctly
t.showTrainNo()
t.getStatus()
t.bookStatus("BBSR", "HYD")
