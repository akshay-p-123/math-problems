# math-problems
Generates random addition, subtraction, multiplication, and division problems. 

I created this project for the 'Website Development Intern' position I currently hold at a local tutoring company. The GUI was not the primary focus of this project, moreso the functionality. __This program is not in active use, it is only to demonstrate the concept.__ The intention was to create a program that helps grade-school age children learn basic arithmetic in a fun and competitive way.

This program currently has no identified bugs. However, I plan to add additional functionality (storing account and leaderboard data using SQL, the ability to create new user accounts, back buttons, and more intuitive UX).

The code style for this project is object-oriented, possessing modules for the GUI and leaderboard.

This project is created in Python using the tkinter module, which I chose because of its lightweight API and straightforward implementation. On Windows, tkinter is included in the standard Python 3 installation, so no further installation is needed if you have Python installed.
On MacOS, follow this [tutorial](https://www.geeksforgeeks.org/how-to-install-tkinter-on-macos/) to install tkinter. 
On Linux, follow this [tutorial](https://www.geeksforgeeks.org/how-to-install-tkinter-on-linux/).
To install Python on all systems, use this [link](https://www.python.org/downloads/).

Once downloaded, make sure to run main.py.
In shell:
`python main.py`

As this program is intended for children, the GUI uses bright colors and has minimal options to reduce confusion. The flow of the program is relatively self-explanatory.
![image](https://github.com/akshay-p-123/math-problems/assets/80610931/13cb7d48-0cd5-4a32-ac09-89aeba56571b)

First, log in using one of the following accounts (currently 5 available):

 Usernames|Passwords 
 :----------:|:---------: 
 user1|abcd  
 user2|1234
 user3|efgh
 user4|5678
 user5|4321
 
You will then be taken to this screen, where you have the choice of seeing the leaderboard or being taken to another screen where you can choose the type and number of questions to be answered.


![image](https://github.com/akshay-p-123/math-problems/assets/80610931/69cb7aa2-e30b-45e5-bfe5-2f332e22cc0f)





![image](https://github.com/akshay-p-123/math-problems/assets/80610931/0820297a-d7e0-466a-b94e-7222849ab54c)






After choosing the question type and number, you will be able to start answering questions. 

![image](https://github.com/akshay-p-123/math-problems/assets/80610931/7b383306-bde0-4e51-bce6-b04293caa1fe)
You get two tries per question and once you get it wrong twice, it displays the correct answer and prompts you to move on to the next question. 




Once you're done answering questions, it displays your score. 10 points are awarded for a correct answer on the first try, 5 points for getting it right on the second try, and none for an incorrect answer. 
![image](https://github.com/akshay-p-123/math-problems/assets/80610931/3bc7648a-0cde-4e26-a8f8-ac54b17efc57)
In this case, I got three correct answers on the first try and one wrong answer.




Pressing the 'Leaderboard' button takes you to this screen:
![image](https://github.com/akshay-p-123/math-problems/assets/80610931/605b783c-aa9a-4564-8802-1b99f8def921)
The leaderboard shows the top five scores and the current user's score if they aren't in the top five. In this case, user1 has the second-highest score.





__A special thanks to the [tkinter docs](https://docs.python.org/3/library/tk.html)__



 
 
 
