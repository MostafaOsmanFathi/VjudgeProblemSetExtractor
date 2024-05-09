from bs4 import BeautifulSoup
def scrape(page):
    """
    it takes html code of Vjudge contest on your local machine
    anlyze it and extract all problem set
    :param page:
    :return:
    """
    soup=BeautifulSoup(page,'html.parser')
    tabelList=soup.find_all('a', target='_blank')
    problemSet=[]
    for i in tabelList:
        ss=i.get_text(strip=True)
        if len(ss.split())==2:
            problemSet.append(ss)
    return problemSet


HtmlFilePath=input("Enter the path of the Html File:")
HtmlFile=open(HtmlFilePath,'r')
PageContent=HtmlFile.read()
list=scrape(PageContent)
for problem in list:
    Judge,id=problem.split()
    print(Judge,"\t|\t",id,"\t|\t1\t|")
HtmlFile.close()