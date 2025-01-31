# Link Checker 🔗✅  

When I submitted my thesis, I had to manually check every link in my bibliography to make sure they were still accessible on the day of submission. Clicking through dozens of links was frustrating and time-consuming. So instead of wasting time, I wrote a Python script to automate the whole process! 🚀

Now, anyone who has the same problem can just run this script and let it do the work. No more clicking every link one by one! Just follow the instructions below, and you’re good to go.

## Main Features  
✅ Extracts all links from a given text file  
✅ Checks if URLs return `200` (OK) or an error (`404`, `403`, etc.)  
✅ Handles bot protection with custom headers  
✅ Can be extended to use Selenium for JavaScript-heavy sites  

## Usage  
1. Install dependencies:  
   ```sh
   pip install requests

## Future Improvements
- Export results to a CSV file
- Multi-threading for faster link checking
- Handling CAPTCHA-protected sites
