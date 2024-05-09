# VJudge Problem Set Extractor

This Python script is designed for extracting problems from VJudge with VJudge format for private contests that can't be cloned. It utilizes the BeautifulSoup library for parsing HTML.

## Dependencies
#### - python 3
#### - BeautifulSoup4 (bs4)

## How to use?
1. Download the HTML page of the contest from VJudge that you want to extract problems from.
2. Get the path of the downloaded HTML file.
3. Run the program and provide the path to the HTML file.
4. The program will automatically find the problems with their IDs and format them in VJudge problem set format.
5. Add the problem set to Vjudge with Vjudge Format
### How to Run?
#### How to Run in powerShell or in bash 

```
python main.py
```

### How to download Contest as Html File?
- ![Alt Text](images/SaveWebSiteAsHtml.jpg)
- #### then you select Save as 

### Program Run
- ![Alt Text](images/ProgramRun.png)
- #### Run the program

- ![Alt Text](images/HtmlPath.png)
- #### Enter path of the Html Contest File

### OutPut Format

- #### the output will be in Vjudge Format Like the picture below
- ![Alt Text](images/OutPut.png)


### How to use the Vjudge Format on Vjudge 

- #### 1. Go to any group and Choose Arrange Contest
![Alt Text](images/VjudgeArangeContest.png)

- #### 2. Go Down to the Problem Set !
    ![Alt Text](images/ProblemSet.png)

- #### 3. Press on Edit Button !
    ![Alt Text](images/EditButoon.png)
- 
- #### 4. Copy the output of the code and past in the problem set!
    ![Alt Text](images/AfterPast.png)
- 
- #### 5. then you will found the problem set exist in the problem set!
    ![Alt Text](images/ProblemSetAfterAddingProblems.png)
