Numbr_Fib=$1 #User input for number of sequences of Fibinachhi they would like to undergo

F1=0 #First Number  Variable
F2=1 #First Second Variable

echo "The Fibonacci series for $1 sequences is : "   #Display prompt

counter=0
LIMIT=$1 ##Limit is what the user asks for
while [ $F1 -le $LIMIT ] #For each increment of the series do the below formula
do
    echo  "$F1 "  #Echo the first number of the fibinacchi which is actually the outcome..(hard to explain)
    fn=$((F1 + F2))     #F2 is the outbound number you are adding to the fibinacchi to change it
    F1=$F2
    F2=$fn
    let "counter += 1"                     #Fn is the formula for adding F2 and F1
    #The above is showing how fibinacchi replaces the incoming numbers with reocurring ones
done
# End of for loop
#Tyler Blanco - Spitzley 206
#Run it by ./lab5.sh <?>  ?= Beingt he number of sequences you would like to perform




