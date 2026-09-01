from playwright.sync_api import page,export

def testlaunch_navigate_url(page:page);
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    # Fetch URL of Application
    url=page.url
    print("URL of the Application :"+url)
    # Fetch Title of the Application
    title=page.title()
    print("Title of the Application :"+title)