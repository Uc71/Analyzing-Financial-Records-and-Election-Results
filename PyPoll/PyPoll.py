import csv
import os
import sys
PyPollStuff = os.path.join("Resources","PyPollData.csv")
with open(PyPollStuff, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    Khancount=0
    Ccount=0
    Licount=0
    OTooleycount=0
    votescount=0
    for row in csvreader:
        if row[2]=="Khan":
            Khancount=int(Khancount+1)
            votescount=int(votescount+1)
        elif row[2]=="Correy":
            Ccount=int(Ccount+1)
            votescount=int(votescount+1)
        elif row[2]=="Li":
            Licount=int(Licount+1)
            votescount=int(votescount+1)
        elif row[2]=="O'Tooley":
            OTooleycount=int(OTooleycount+1)
            votescount=int(votescount+1)
    Khanperc=int(100*round(Khancount/votescount,3))
    Cperc=int(100*round(Ccount/votescount,3))
    Liperc=int(100*round(Licount/votescount,3))
    OTooleyperc=int(100*round(OTooleycount/votescount,3))
    cands=[Khanperc,Cperc,Liperc,OTooleyperc]
    print("Election Results")
    print("----------------------------")
    print("Total Votes: "+str(votescount))
    print("----------------------------")
    print("Khan: "+str(Khanperc)+"% ("+str(Khancount)+")")
    print("Correy: "+str(Cperc)+"% ("+str(Ccount)+")")
    print("Li: "+str(Liperc)+"% ("+str(Licount)+")")
    print("O'Tooley: "+str(OTooleyperc)+"% ("+str(OTooleycount)+")")
    print("----------------------------")
    if max(cands)==Khanperc:
        print("Winner: Khan")
    elif max(cands)==Cperc:
        print("Winner: Correy")
    elif max(cands)==Liperc:
        print("Winner: Li")
    elif max(cands)==OTooleyperc:
        print("Winner: O'Tooley")
    with open ("PyPollanalysis.txt", "w") as f:
        print("Election Results", file=f)
        print("----------------------------", file=f)
        print("Total Votes: "+str(votescount), file=f)
        print("----------------------------", file=f)
        print("Khan: "+str(Khanperc)+"% ("+str(Khancount)+")", file=f)
        print("Correy: "+str(Cperc)+"% ("+str(Ccount)+")", file=f)
        print("Li: "+str(Liperc)+"% ("+str(Licount)+")", file=f)
        print("O'Tooley: "+str(OTooleyperc)+"% ("+str(OTooleycount)+")", file=f)
        print("----------------------------", file=f)
        if max(cands)==Khanperc:
            print("Winner: Khan", file=f)
        elif max(cands)==Cperc:
            print("Winner: Correy", file=f)
        elif max(cands)==Liperc:
            print("Winner: Li", file=f)
        elif max(cands)==OTooleyperc:
            print("Winner: O'Tooley", file=f)