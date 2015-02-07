minezy_proto
============
This project was made possible by the <a href="http://www.knightfoundation.org/grants/201448427/">Knight Prototype Fund</a><br>
Try the running demo at <a href="http://minezy.org">http://minezy.org</a>


---------------------------
To run Minezy on your own:

First install Neo4j database http://www.neo4j.org/ (v2.0+)<br>
Start Neo4j and have it running at localhost:7474<br>

Install python modules:
pip install flask flask-cors flask-Cache py2neo(2.0+) beautifulsoup4 nltk email-reply-parser argparse

Then under ./minezy_api/ launch:

<b>python ./run_ui.py<br>
python ./run_server.py</b><br>

Open browser to: localhost:8080/
You should see the Minezy title page, but there won't be anything to navigate until you load Neo4j with email data.
Do that by running:

<b>python ./load_files.py -d depot_dir</b>

The [depot_dir] parameter should point to a parent folder of a parsed PST dump (eg: as generated by <a href='http://www.five-ten-sg.com/libpst/rn01re01.html'>readpst</a> tool)
Once complete, reload localhost:8080/ and start minezying.
