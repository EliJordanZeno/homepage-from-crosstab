<h1>Homepage from Crosstab</h1>

<p>This repo houses a python script to generate excel homepage from a downloaded crosstab excel spreadsheet.</p>

# Steps to run the script

<ol>
    <li>Download this repo to your machine locally</li>
    <li>Navigate to the downloaded repo in the command line
    <ul><li>Alternatively, open the folder in VScode</li></ul>
    </li>
    <li>Activate the virtual environment in the command line
    <ul>
    <li>Mac: source crosstab_venv/bin/activate</li>
    <li>Windows: I'm not sure, I think you have to make a new one. <a href="https://docs.python.org/3/library/venv.html">Here's the documentation</a></li>
    </ul>
    <li>Ensure all the required packages are installed using <b>pip install -r requirements.txt</b></li>
    <li>Now, move the downloaded (source) crosstab file into the same folder as crosstab_gen.py</li>
    <ul><li>Remember to clear out any questions you don't want to show up in the final workbook (screeners, demos)</li>
    <li>And rename the audiences</li>
    </ul>
    <li>Finally, open <em>crosstab_gen.py</em> and change the file paths at the bottom of the file to reflect the files you are working with (input and output)</li>
    <li>Now run the script either from the command line with <em>python crosstab_gen.py</em> or by clicking the play button in VSCode</li>
    <li>You should now have a new file that has the name you gave it in the script.</li>
    </li>
    <li>This file is now ready to run the <u>links</u> and <u>formatting</u> macros found <a href="https://djeholdingsdrive.sharepoint.com/:f:/r/sites/SPTeamRepo2.0/Shared%20Documents/8.%20Innovation%20+%20Development/S+P%20Custom%20Code/Crosstabs%20Generation%20Macros?csf=1&web=1&e=nxJDj0">here</a></li>
    <li>After the links and formatting macros, move all the options links into the D column with the questions and use the AddWhitespaceMacro on each of the question cells.
    <ul>
        <li>Mac: CMD + Shift + I</li>
        <li>Windows: Ctrl + Shift + I</li>
    </ul></li>
    <li>Check with Eli French with the final file for any errors, missing questions, audiences, names, etc.</li>
<ol>

<h3>PLEASE BRANCH ANY CHANGES</h3>
