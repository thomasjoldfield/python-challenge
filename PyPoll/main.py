#always start with pandas
import pandas as pd

#Allow to select from similar files(provided formatting consistent)
whichFile = input("Election Results [1] or [2]? ")
electionLocation = "../../../Resources/PyPoll/raw_data/election_data_" + str(whichFile) + ".csv"

election_df = pd.read_csv(electionLocation)
#election_df.head()

''' What we're aiming for:

Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------'''
#grabbing total is easy, let's just do this now and sit on it
totalVotes = election_df["Voter ID"].nunique()

#create a list of candidates
candidates = election_df["Candidate"].unique()

#group by candidates, adds sensible index and aggregates
totalVotesGrouped = election_df.groupby("Candidate")
electionResults = totalVotesGrouped.count()
#print(electionResults)

#make our results a little prettier, get percents in there
electionResults["votePercent"] = electionResults["Voter ID"]/totalVotes
electionResults = electionResults.rename(columns = {"Voter ID":"voteTotal"})
electionResults[["voteTotal", "votePercent"]]

#nice upgrade over last exercise: the .idxmax method 
winner = electionResults.voteTotal.idxmax()
#print(winner)

print("Election Results")
print("---------------------------")
for name in candidates:
    votes = electionResults["voteTotal"][name]
    percent = electionResults["votePercent"][name]
    print(name + ": " + str(percent*100) + "% (" + str(votes) + ")")
    
print("---------------------------")
print("Winner: " + winner)
print("---------------------------")

outputName = "Election Results "+str(whichFile)
print("Creating Election Results")
try:
    file = open(outputName + ".txt", 'w')
    file.write("Election Results\n")
    file.write("----------------------------\n")
    for name in candidates:
        votes = electionResults["voteTotal"][name]
        percent = electionResults["votePercent"][name]
        file.write(name + ": " + str(percent*100) + "% (" + str(votes) + ")\n")
    file.write("----------------------------\n")
    file.write("Winner: " + winner + "\n")
    file.write("----------------------------\n")    
    file.close()
    print("File " + outputName + " created.")
except:
    print("Well, that didn't work")