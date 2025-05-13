#Alonzo Aldape
#4/13/25
#P4HW1
#The goal of this project is to make a loop to calculate a grade based on inputs and it is able to drop the lowest grade and work with different combos.

#Pseudocode
#1.)Ask how many scores they'd like to enter
#2.)display a number for each score inputed so it is in order for how many they are going to enter
#3.)If a score is not between 1-100 give error and ask them to redo it, if not proceed to next number on list
#4.)when all scores are entered make sure they show results by giving lowest, average, and letter grade and also giving list dropping lowest grade
#5.)display these results ending with the final letter grade determined by what the average is based on the previous caluclation and lining it up with the correct letter grade


num_of_scores = int(input("How many scores do you want to enter?  "))
print()

scores_collected = []
entered_scores = 0

while entered_scores < num_of_scores:
    user_score = float(input(f"Enter score #{entered_scores + 1}: "))

   
    while user_score < 0 or user_score > 100:
        print("INVALID Score Entered!!!!!")
        print("Score should be between 0 and 100")
        user_score = float(input(f"Enter score #{entered_scores + 1} again: "))

    scores_collected.append(user_score)
    entered_scores += 1

print()
print()

print("------------ Results -----------")


lowest_score = min(scores_collected)
scores_collected.remove(lowest_score)
adjusted_total = sum(scores_collected)
average = adjusted_total / (num_of_scores - 1)

if average >= 90:
    final_grade = 'A'
elif average >= 80:
    final_grade = 'B'
elif average >= 70:
    final_grade = 'C'
elif average >= 60:
    final_grade = 'D'
else:
    final_grade = 'F'

print("Lowest Score  :", lowest_score)
print("Modified List :",scores_collected)
print(f"Scores Average: {average:.2f}")
print("Grade         :", final_grade)

print("--------------------------------------")
