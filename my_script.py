import os

# GitHub Secret से Token को Load करो
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  

if GITHUB_TOKEN:
    print("✅ GitHub Token Successfully Loaded!")
else:
    print("❌ GitHub Token Not Found!")

# अब इस Token को API Calls में Use कर सकते हो
