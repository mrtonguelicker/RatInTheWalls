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
#This will make the download happen in your Desktop Folder
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

Everytime you sit down to code, follow this cycle: 

...
...
...

## Common Problems 

...
...
...
