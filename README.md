# TimeTickQuiz - A Magic Library Adventure!  

## The Premise  
Hello, Recruit !  
You are in a magical library called TimeTick Library, where books come to life and ask you fun questions! But there’s a magic rule: You shuld answer each question in 15 seconds before the book closes and the magic fades away.  

The library has a special book called the Open Trivia API, filled with questions about animals, movies, history, and more. Your job is to make a quiz game that talks to this book, asks its questions, and helps you become the best reader in the library. You need to be quick and smart to win a golden star!

## The Challenge: TimeTickQuiz  
Your task is to make a quiz game in Python that runs on the `CLI`. It’s a race against the magic book’s timer, so you gotta be fast!  



### Your Quiz Shud:
- At the start of the quiz, prompt the user for their username and store it, along with their score, which shud update regularly as their score increases with each correct answer.
- Talk to the Open Trivia Database API to get questions.
- Let the user pick how many questions they want (like 1 to 20), how much time for each question (like 10 to 30 seconds), the catrogery (like animals or sports), how hard (easy, medium, hard), and question type (many choices or yes/no).
- Use the time limit user picked for each question with a timer.
- Use the rich library to color the console and make it look good (like blue for questions, green for correct, red for wrong).
- Tell the user if their answer is right or wrong right away.
- Count u r score and add points for correct answers.
- Show the final score at the end with a nice message.
- Save the score so the user can see it later.

### What Do U Learn?  
- How to use a web API in Python to get data  
- How to make a fun game on the computer  
- How to add a timer using threads for fast action  
- How to use JSON to save and read info  
- How to make the console look pretty with the `rich` library  

## Get Started  
Here’s how to make your TimeTickQuiz game:  

### 1. Make a Copy of the Directory Structure in Your Local Machine  
Make the copy of the directory strructure on your system:  
``` bash
TimeTickQuiz-2/
├── src/
│   ├── main.py
│   ├── quiz_engine.py
│   ├── user_profile.py
│   ├── utils.py
├── profiles.json
├── requirements.txt
├── README.md
```

### 2. Copy the Skeleton Code and Paste in Your Machine  
Copy the skeleton code of `all the files` from the repository and paste it in your `Directory`.  

### 3. Navigate to the Src Folder  
Type this in your computer:  
```bash
cd TimeTickQuiz/src
```
### 4. Create a Venv
Make a virtual space to keep your game safe. This helps avoid problems with other Python projects.

```bash
python3 -m venv venv
source venv/bin/activate
```
### 5. Install the Packages Required
Type this to get the tools u need:

```bash
pip install -r requirements.txt
```
### 6. Write Your Code
Edit the logic in the files:
``` bash
- main.py
- quiz_engine.py
- utils.py
- user_profile.py
```
### 7. Run the App
Type this to start your game:

``` bash
python3 main.py
```
---
Need resources? Check out the [RESOURCES.md](https://github.com/Kota-Jagadeesh/TimeTickQuiz-2/blob/main/RESOURCES.md) file for more!
---
Let’s play, Reader! The book is closing! 📚  
- Can u win the golden star?

``` bash
Happy coding! ✨
```