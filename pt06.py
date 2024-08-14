#While
i = 1
while i < 6:
    if i == 3:
        continue
    if i == 2:
        break
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#For
frutti = ["mela", "banana", "cocco"]
aggettivi = ["buono", "cattivo", "normale"]
for frutta in frutti:
    for aggettivo in aggettivi:
        print(frutta.capitalize(), aggettivo)