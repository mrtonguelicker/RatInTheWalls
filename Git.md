# Git guide (for the team)

If you guys are not familiar with GitHub at all, I would highly recommend watching a few youtube videos and setting it up that way. 

It's going to be much easier to understand what you're doing if you're following a video tutorial. 

I'll link some videos on how to download git on Windows and Mac. If you're using Linux like me, learn how do it yourself. 

## 1. Installation 

Videos: 
- Windows: https://youtu.be/wDRoduig_98. 
- Mac: https://www.youtube.com/watch?v=R9Efdq3Fj-A.

If you'd rather not watch the videos: 
- Windows: Download Git from https://git-scm.com/downloads and run the installer. Use default options in the installer. 
- Mac: Open Terminal and run 'xcode-select --install'.

## 2. Cloning the Repository

After being done with the installation, you will need to 'download' the repository to your computer. This is how you will be able to program and make changes to the code. This process is called 'cloning' the repository. 

For our project, open Terminal on Mac or Command Line on Windows and type in: 

```bash 
#This will download the repository in your Desktop Folder
cd Desktop 
git clone https://github.com/mrtonguelicker/RatInTheWalls
```
This downloads the whole project to your folder. You only need to do the cloning once.

## 3. Configuring your account

You will now need to 'sign-in' to your github account. These commands should work on both Windows and Mac, but if for whatever reason, they do not, look it up on YouTube.

If you still cannot figure it out, you can always ask me for help.

```bash
git config --global user.name "insert_your_username"
git config --global user.email "your@email.com" #with which you created your github account
```

## How to work

Everytime you sit down to code, follow this: 

- After having the repository cloned, the first step everyday is to do a: ```bash git pull ```
This is to pull in any changes made by other people first before you start working.
- We will be working with branches in this project. Branches are essentially work-in-progress- copies of the code. 
- Never code on the main branch directly. This is to have a protected copy of working code that no on can mess with, specially in the early stages of making this project when we'll be changing things constantly.
- You can use ```bash git checkout -b whatever-branch-name``` to create a branch that you can work and test things in. Please use meaningful names so that other are able to understand what the branch is meant for without reading all the code. Try to keep the name one to two words seperated by a "-".
- When you create new files in a branch, they won't automatically be uploaded to github. Add them by using ```bash git add .``` to add all the files in your folder to be uploaded to Github. 
- Use git commit to save checkpoints for your code: ```bash git commit -m "message_about_changes"```. Think of these as save points that you can always load back no matter how many changes you make after this. Keep the messages in the commit messages meaningful (don't do something generic like: new changes).
- When you're ready to upload code to your Github branch, use ```bash git push origin your-branch-name```. **Remember:** this always uploads your lastest save, **not** what you have on your computer, so make sure to commit before pushing. 


I'll add more stuff here about how to merge with main by creating a pull request later. -Pragyay 

## Common Problems 

...
...
...
