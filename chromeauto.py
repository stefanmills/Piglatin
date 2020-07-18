import webbrowser as wb

def chromeauto():
    chrome_path="/opt/google/chrome/google-chrome" #executable chrome path
    websites={"twitter.com",
              "gmail.com",
              "coursera.org",
              "udemy.com"}
    for url in websites:
        print("Opening "+url)
        wb.get(chrome_path).open(url)

chromeauto()