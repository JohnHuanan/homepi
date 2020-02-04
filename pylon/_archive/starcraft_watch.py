
# This

# set pylon to off

# while  (true)

    # if time = 06:00 then 

        # connect internet; grab page
        
# read text file

input = open ('liquipedia.net_starcraft2_Premier_Tournaments.html')

text = input.read()
sub = "2020-03-01"

print(text.find(sub))

for i in range (text.find(sub), (text.find(sub)+10)):
    print(text[i])
    
# TODO

# bestimme aktuelles Jahr

# suche alle start und enddaten für aktuelles Jahr

#with open ('test.txt') as f:
#    for line in f:
#        if line == " <td>$300,000":
#            print(line)

        # collect begin end (and title) of tournaments; try search Jan, Feb, Mar..

        # if current.date >= as begin and <= end then activate pylon
        
        # else if pylon is on then deactivate pylon

