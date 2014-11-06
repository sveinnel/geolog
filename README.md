GeoLog
======

The GeoLog is a datalogger based on an [project](https://github.com/NorthernWidget/ALog-BottleLogger) 
developed by [Andrew D. Wickert](http://instaar.colorado.edu/~wickert/) and was built in the course Mechatronics I at Reykajvik University, fall 2014. 

The GeoLog is a modular platform for datalogging built on a 
[Arduino Mega 2560](http://arduino.cc/en/Main/arduinoBoardMega2560). This version usees
[Wixels](http://www.pololu.com/product/1336) for communicating with sensors and 
[GE864 Evaluation Board with SM5100B GSM module](https://www.sparkfun.com/products/retired/9311) for GPRS and SMS
communications. 

Application
-----------
The main application of the data logger is a telemetry device for returning data. Good telemetry communication for a data logger eases the process of maintenance checks and enables more involved researches.
Telemetry via [GSM network is available throughout most part of Iceland](http://www.vodafone.is/internet/farnet/utbreidsla/) where the device will be tested. With GSM shield on the data logger one might be able to monitor data logging in most places in Iceland. Radio coverage can be quite good over long distance. 
The [XBee](http://www.digi.com/products-overview) modules with Arduino support come with radio ranges for up to 60km. If the data logger is equipped with the [XBee](http://www.digi.com/products-overview) module the researcher might set up a ground station with in a 60km radius.
[Iridium](https://www.iridium.com/default.aspx) satellite phone might be connected to the data logger to enable good coverage in remote areas. [Iridium](https://www.iridium.com/default.aspx) phone has coverage anywhere in the world were there is a clear view of the sky, by connecting to any of the 66 iridium satellites in orbit around the earth\cite{iridium}. The GeoLog is a standard platform designed for GSM ready for integration of  [XBee](http://www.digi.com/products-overview) and [Iridium](https://www.iridium.com/default.aspx).

Layered Structure
-----------------
![Layered Structure](https://raw.githubusercontent.com/sveinnel/geolog/master/Images/Layering.png "Layered Structure")

Class Diagram
-------------
![Class Diagram](https://raw.githubusercontent.com/sveinnel/geolog/master/Images/ClassDiagram.png "Class Diagram")

Web Server
----------
The web server is a simple Flask-Restful Api and a human readable route using Flask. This server was just set up as a proof of consept but works fine for testing application. All authentication and security features have yet to be implemented.

Copyright
---------
######Copyright (C) 2014-2015, Páll Svavar Helgason, Sindri Ólafsson, Sveinn Elmar Magnússon and Þór Tómasarson.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

######Contact:
Páll Svavar Helgason pallsh12@ru.is, 
Sindri Ólafsson sindrio12@ru.is, 
Sveinn Elmar Magnússon sveinnm12@ru.is,
Þór Tómasarson thortom12@ru.is
