#we need more pandas!
import pandas as pd

#allows you to run for multiple files without changing the code
whichFile = input("Budget file [1] or [2]? ")

budgetLocation = "../../../Resources/PyBank/raw_data/budget_data_" + str(whichFile) + ".csv"

budget_df = pd.read_csv(budgetLocation)
#Set month to index, if you wanna... budget_df = budget_df_original.set_index("Date")
#checkpoint 1
budget_df.head()

#get total number of months
totalMonths = budget_df["Date"].nunique()
#checkpoint 2
print("Total Months: " + str(totalMonths))

#get total revenue value
totalRevenue = budget_df["Revenue"].sum()
#checkpoint 3
print(totalRevenue)

#for comparison between months, we need the columnn shift
budget_df["RevenueShift"] = budget_df["Revenue"].shift(1)
#checkpoint 4
budget_df

#capture the shift in a new field for change in revenue
budget_df["RevenueChange"]=budget_df["Revenue"]-budget_df["RevenueShift"]
#checkpoint 5
budget_df

#grab the mean of those changes 
AverageChange = budget_df["RevenueChange"].mean()
#checkpoint 6
print("Average Change in Budget: $"+str(AverageChange))

#calculate max of the changes
MaxChange = budget_df["RevenueChange"].max()
#checkpoint 7
print(MaxChange)

#calc min change
MinChange = budget_df["RevenueChange"].min()
#checkpoint 8
print(MinChange)
#example code
#only_billys = df.loc[df["first_name"] == "Billy",:]

#then grab the date that corresponds with maxchange
MaxDate_df = budget_df.loc[budget_df["RevenueChange"] == MaxChange, "Date"].values[0]
#checkpoint 9
print(MaxDate_df)

#and date for minchange
MinDate_df = budget_df.loc[budget_df["RevenueChange"] == MinChange, "Date"].values[0]
#checkpoint 10
print(MinDate_df)

#print report in terminal 
print("")
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalMonths))
print("Total Revenue: $" + str(totalRevenue))
print("Average Revenue Change: $"+str(AverageChange))
print("Greatest Increase in Revenue: " + MaxDate_df + " ($" + str(MaxChange)+")")
print("Greatest Decrease in Revenue: " + MinDate_df + " ($" + str(MinChange)+")")

#write report to text file
outputName = "Budget Summary "+str(whichFile)
print("Creating Budget Summary")
try:
    file = open(outputName + ".txt", 'w')
    file.write("Financial Analysis" + '\n')
    file.write("----------------------------" + '\n')
    file.write("Total Months: " + str(totalMonths) + '\n')
    file.write("Total Revenue: $" + str(totalRevenue) + '\n')
    file.write("Average Revenue Change: $"+str(AverageChange) + '\n')
    file.write("Greatest Increase in Revenue: " + MaxDate_df + " ($" + str(MaxChange)+")" + '\n')
    file.write("Greatest Decrease in Revenue: " + MinDate_df + " ($" + str(MinChange)+")" + '\n')
    file.close()
    print("File " + outputName + " created.")
except:
    print("Well, that didn't work")

