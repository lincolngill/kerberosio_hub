#!/usr/bin/env python3
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():

    html = '''<!DOCTYPE html>
<html>
    <head>
        <title>Security Cameras</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

body {
  font-family: Arial, Helvetica, sans-serif;
}

/* Style the header */
.header {
  background-color: #EAEDED;
  padding: 5px;
  text-align: left;
  font-size: 10px;
  color: #1B4F72;
}

/* Create three equal columns that floats next to each other */
.column {
  float: left;
  /* width: 50%; */
  padding: 5px;
  /* height: 500px; Should be removed. Only for demonstration */
  color: #1B4F72;
  text-align: center;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Style the footer */
.footer {
  background-color: #EAEDED;
  padding: 5px;
  text-align: left;
  color: #1B4F72;
}

/* Responsive layout - makes the three columns stack on top of each other instead of next to each other */
@media (max-width: 600px) {
  .column {
    width: 100%;
  }
}
</style>
    </head>
    <body>
        <div class="header">
            <h1>Security Cameras - Live feed</h1>
        </div>

        <div class="row">
            <div class="column" style="background-color:#BFC9CA;">
                <img style="-webkit-user-select: none;margin: auto;" src="http://192.168.1.61:8889/" width="640" height="480"><br/>
                Camera 1 - Rumpus Room<br/>
            </div>
            <div class="column" style="background-color:#D5DBDB;">
                <img style="-webkit-user-select: none;margin: auto;" src="http://192.168.1.6:8889/" width="640" height="480"><br/>
                Camera 2 - Entrance and Stairs<br/>
            </div>
        </div>

        <div class="footer">
            <div id="clockbox" color:#FF6666;"></div>
<script type="text/javascript">
var tday=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
var tmonth=["January","February","March","April","May","June","July","August","September","October","November","December"];

function GetClock(){
    var d=new Date();
    var nday=d.getDay(),nmonth=d.getMonth(),ndate=d.getDate(),nyear=d.getFullYear();
    var nhour=d.getHours(),nmin=d.getMinutes(),nsec=d.getSeconds(),ap;

    if(nhour==0){ap=" AM";nhour=12;}
    else if(nhour<12){ap=" AM";}
    else if(nhour==12){ap=" PM";}
    else if(nhour>12){ap=" PM";nhour-=12;}

    if(nmin<=9) nmin="0"+nmin;
    if(nsec<=9) nsec="0"+nsec;

    var clocktext=""+tday[nday]+", "+tmonth[nmonth]+" "+ndate+", "+nyear+" "+nhour+":"+nmin+":"+nsec+ap+"";
    document.getElementById('clockbox').innerHTML=clocktext;
}

GetClock();
setInterval(GetClock,1000);
</script>
        </div>
    </body>
</html>
'''
    return html

if __name__ == "__main__":
    # Use waitress server rather than development flask
    #app.run(host='0.0.0.0', port=8080)         
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)