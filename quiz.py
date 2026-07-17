questions = {
    "What is the capital of India?\n1. Mumbai\n2. Delhi\n3. Kolkata\n4. Chennai": "2",
    "Which language is this program written in?\n1. Java\n2. C++\n3. Python\n4. Ruby": "3",
    "How many continents are there?\n1. 5\n2. 6\n3. 7\n4. 8": "3",
    "What is 5 + 3?\n1. 7\n2. 8\n3. 9\n4. 10": "2",
    "What is the largest planet in our solar system?\n1. Earth\n2. Saturn\n3. Mars\n4. Jupiter": "4"
}

score = 0

for question in questions:
    print("\n" + question)
    answer = input("Enter your choice (1-4): ")
    correct_answer = questions[question]

    if answer == correct_answer:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer was option", correct_answer)

print("\nQuiz Finished")
print("Your final score is:", score, "out of", len(questions))