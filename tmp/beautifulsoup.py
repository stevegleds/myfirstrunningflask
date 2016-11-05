import urllib2
import BeautifulSoup

def main():
    url = "http://allrecipes.com/Recipe/Slow-Cooker-Pork-Chops-II/Detail.aspx"
    data = urllib2.urlopen(url).read()
    bs = BeautifulSoup.BeautifulSoup(data)

    ingreds = bs.find('div', {'class': 'ingredients'})
    ingreds = [s.getText().strip() for s in ingreds.findAll('li')]

    fname = 'PorkChopsRecipe.txt'
    with open(fname, 'w') as outf:
        outf.write('\n'.join(ingreds))

if __name__=="__main__":
    main()