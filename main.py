#Flashcard app 
#Users can input a question, and an answer
#All questions and answers are stored in a csv file 
#the computer then picks a question from random and waits for the user to answer it, it'll then show the user the answer to see if they got it correct 
import csv
import random

header = ["id", "question", "answer"]
row = []
def flashcard_app():
    while True:
        print("Welcome to the flashcard app")
        print("Remember, each time you close the app it'll delete your flashcards")
        print("1. Add a question and answer")
        print("2. Test yourself")
        print("3. Delete all flashcards")
        print("4. Exit the game...")
        choice = input("Choose an option 1-4: ")
        
        if choice == "1":
         flashcard = questions_Answers()
         f = open("flashcardData.csv", mode="a", newline="")
         writer = csv.writer(f)
         writer.writerow(header)
         writer.writerow(flashcard)
         return
        elif choice == "2":
            try: 
                f = open("flashcardData.csv")
                reader = csv.reader(f)
                next(reader)
                questions = list(reader)
                if not questions:
                    print("No questions are available. Please add some first.")
                    return
                question = random.choice(questions)
                print(f"Question: {question[1]}")
                input("Your Answer: ")
                print(f"The correct answer is: {question[2]}")    
            except FileNotFoundError: 
                    print("No flashcards found. Please add some first.")
        elif choice == "3":
            f = open("flashcardData.csv", mode="w")
            f.truncate()
            f.close()
        elif choice == "4":
            return

def questions_Answers():
    question = input("Please enter your question: ")
    answer = input("Please add the answer to your question: ")
    
    number = random.randint(1, 1000)
    
    return [number, question, answer]

def main():
    flashcard_app()

if __name__ == "__main__":
    main()
