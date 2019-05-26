# sydneytrains
This project uses the [TfNSW Open Data](https://opendata.transport.nsw.gov.au/) [Public Transport - Realtime Vehicle Positions](https://opendata.transport.nsw.gov.au/dataset/public-transport-realtime-vehicle-positions) API to display the realtime positions of Sydney trains.

## Features
- Colour-coded train lines plotted on a base map
- Realtime positions of Sydney and intercity trains, refreshed every 5 seconds
- Mouseover popups displaying route, number of carriages and train set type

## How to run
1. `pip install -r requirements.txt`
2. `python testServer.py`

## Built with
- [TfNSW Open Data](https://opendata.transport.nsw.gov.au/), [Public Transport - Realtime Vehicle Positions API](https://opendata.transport.nsw.gov.au/dataset/public-transport-realtime-vehicle-positions)
- [Mapbox](https://www.mapbox.com/) - base map, markers and popups
- Python - general data wrangling and web server
- [Protocol buffers](https://developers.google.com/protocol-buffers/) - serialising structured data 

## Project website
[https://sydneytrains.herokuapp.com/](https://sydneytrains.herokuapp.com/)

## Acknowledgements
Ben Mitchell, for his patience, hacky server workarounds, and debugging prowess.