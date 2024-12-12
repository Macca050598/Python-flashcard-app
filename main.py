#Flashcard app 
#Users can input a question, and an answer
#All questions and answers are stored in a csv file 
#the computer then picks a question from random and waits for the user to answer it, it'll then show the user the answer to see if they got it correct 
import csv
import random

header = ["id", "question", "answer"]
    
def flashcard_app():
    print("Welcome to the flashcard app")
    print("Remember, each time you close the app it'll delete your flashcards")
    print("1. Add a question and answer")
    print("2. Test yourself")
    print("3. Exit the game...")
    choice = input("Choose an option 1-3")
    
    if choice == "1":
       flashcard = questions_Answers()
       f = open("flashcardData.csv", mode="w", newline="")
       writer = csv.writer(f)
       writer.writerow(header)
       writer.writerow(flashcard)
    elif choice == "2":
        question_picker()
    elif choice == "3":
        return
    

def questions_Answers():
    question = input("Please enter your question: ")
    answer = input("Please add the answer to your question: ")
    
    number = random.randint(1, 1000)
    
    return [number, question, answer]


def question_picker():
    question = ["Test", "Twlooqw"]
    print(random.choice(question))

def main():
    flashcard_app()

if __name__ == "__main__":
    main()
