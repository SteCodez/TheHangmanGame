![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Project-3- The Hangman Game


## Goals
***

* To have a challenging game of Hangman
* To have multiple options.
* To have a seperate image for game completion.
* To have messages acknowledging completion or failure to complete the game.

---
---
## Technologies
***

* JavaScript
* VSCode
* GitHub
* Pylint
* Heroku
* pep8

---
---
## Testing
***

 | What is expected. | Did the element successfully perform its task? If not, why? | How was the issue fixed? | Approved/issue resolved? |
   |-------------| ------------ | ------------- |------------- |
| I expect the program to run when the "Run program" button is pressed on Heroku. | Yes the program ran as expected. | n/a | Yes. |
|I expect all options on the menu to take me to the requested topic. | The program did not take me to each topic as expected, topic 2 would not run properly. | The issue was fixed by removing the topic altogether as no error was shown and I was short on time to properly investigate the bug. | Temporary fix applied, will revisit at a later date. | No. |
| I expect the quit option on the menu to return me to the terminal base fucntion. | The quit button performed as expected. | n/a | Yes. |
| I expect to be shown an error message when I have entered either an invalid number of characters or numbers. | A message was shown requesting the player to input valid options to the game. | n/a | Yes. |
| I expect the hangman figure to update accordingly with each incorrect guess. | The hangman figure updated as expected. | n/a | Yes. |
| I expect the game to show me the hangman escaping upon victory conditions being met. | The escape figure displayed as expected. | n/a | Yes. |
| I expect the game to display all incorrect guessed letters for reference as the player progresses. | The incorrect guesses displayed as expected. | n/a | Yes. |

#### Possible future additions

* A timing system
* More topics
* A easy/medium/hard difficulty setting
* A 2 player system allowing players to compete


#### Unresolved problems


## Deployment
***
---

#### Deploying on Heroku

* Navigate to https://www.heroku.com/ and login or create an account.
* Click the "new" button in the upper right corner and select "create new app".
* Choose an app name and your region and click "Create app".
* Under Config Vars store any sensitive data you saved in .json file. Name 'Key' field, copy the .json file and paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
* Go to the "settings" tab, add the Python build pack and then the node.js build pack (please note they need to be in the correct order of Python above node.js).
* Go to the "deploy" tab and pick GitHub as a deployment method.
* Search for a repository to connect to and select the branch you would like to build the app from.
* If preferred enable automatic deploys and then deploy branch.
* Wait for the app to build and then click on the "View" link which will redirect you to the deployed link.

#### Forking the GitHub Repository
By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

* Log in to GitHub and locate the GitHub Repository.
* At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
* You should now have a copy of the original repository in your GitHub account.

#### Making a local clone
* Log in to GitHub and locate the GitHub Repository.
* Under the repository name, click "Clone or download".
* To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
* Open commandline interface on your computer.
* Change the current working directory to the location where you want the cloned directory to be made.
* Type git clone, and then paste the URL you copied above.
* Press Enter. Your local clone will be created.
