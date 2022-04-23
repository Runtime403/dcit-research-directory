## Deployed app: https://dcit-research-directory.herokuapp.com/

To add more DCIT authors, open the "staffmembers.txt" file and enter the full name of the author followed by a "," and then their google scholar profile ID. Save the file.
<br>
eg. John Doe, 8H34NkAWd
<br>
To get the google scholar profile ID, go to their google scholar profile and in the URL address bar, their ID is located after the "user=" in the address, copy and paste that into the staffmembers.txt file.<br>

<b> To Run Python files, you must install scholarly: </b><br>
See here on how to install scholarly: https://scholarly.readthedocs.io/en/latest/quickstart.html<br>
You must have pip installed on your system to install scholarly. <br>
<br>

To update the most_recent.txt file that outputs the data onto the website, run the pull_cited.py file. <br>
To update the most_cited.txt file that outputs the data onto the website, run the pull_recent.py file. <br>
To update the authors.txt file that outputs data onto the website, run the pull_authors.py file. <br>

<br>
To run these python scripts mentioned above automatically on a weekly basis, follow this video for each script: https://www.youtube.com/watch?v=CAH0B1ErriI <br>
This must be run on a computer that will be deploying the website <br>
