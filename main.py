from bs4 import BeautifulSoup


def scrape(page):
    """
    it takes html code of Vjudge contest on your local machine
    anlyze it and extract all problem set
    :param page:
    :return:
    """
    soup = BeautifulSoup(page, 'html.parser')
    tabelList = soup.find_all('a', target='_blank')
    problemSet = []
    for i in tabelList:
        ss = i.get_text(strip=True)
        if len(ss.split()) == 2:
            problemSet.append(ss)
    return problemSet


HtmlFilePath = input("Enter the path of the Html File:")
HtmlFile = open(HtmlFilePath, 'r')

try:
    with open(HtmlFilePath, "r",encoding="utf-8") as HtmlFile:
        PageContent = HtmlFile.read()
        listOfProblems = scrape(PageContent)
        for problem in listOfProblems:
            Judge, id = problem.split()
            print(Judge, "\t|\t", id, "\t|\t1\t|")
        HtmlFile.close()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("An error occurred:", e)


