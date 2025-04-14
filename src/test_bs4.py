from bs4 import BeautifulSoup

def test_bs4():
    html = "<html><body><p>Test</p></body></html>"
    soup = BeautifulSoup(html, 'html.parser')
    print("BeautifulSoup4 is working correctly!")
    print(f"Found paragraph: {soup.find('p').text}")

if __name__ == "__main__":
    test_bs4() 