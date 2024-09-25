Dinosaur Tea Party Player

By Stephen Hall

These Python programs perform deductions for the children’s board game Dinosaur Tea Party (Restoration Games, 2018). For each program, there are two versions, V1 and V2. They are similar, but they differ in how they choose questions to ask. V1 chooses questions at random, with the stipulation that questions must always reduce the number of remaining possibilities. V2 chooses questions that will eliminate half, or as close to half as possible, of the remaining possibilities.

To get the "purest" data possible, these programs do not use trait tokens ("Switches Answers," "Always Lies," "Always Says No"). This means that all dinosaurs tell the truth, always. Also, the programs make logical deductions about room colors. If a question is asked about a color and a "yes" answer is given, any remaining colors are removed from consideration. Likewise, if a program asks about two colors and gets "no" answers to both, it will not ask about the remaining color. (These parameters ensure that the program doesn't "waste" any questions.)

"DinosaurTeaParty" is the original file, with move-by-move text output.
"DinosaurTeaPartyFunction" is the same program, but cast as a function and without the text output.
"DinosaurTeaPartyPlayer" is the script that plays the game and generates visual output.