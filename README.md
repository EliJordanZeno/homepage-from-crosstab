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
    <li>Finally, open <em>crosstab_gen.py</em> and change the file paths at the bottom of the file to reflect the files you are working with (input and output)</li>
    <li>Now run the script either from the command line with <em>python crosstab_gen.py</em> or by clicking the play button in VSCode</li>
    <li>You should now have a new file that has the name you gave it in the script.</li>
    </li>
<ol>

<h3>PLEASE BRANCH ANY CHANGES</h3>