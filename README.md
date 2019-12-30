# The big picture
This repository is part of the ‘projet transverse’ of the [Advanced Master ValDom](http://www.enseeiht.fr/fr/formation/masteres-specialises/valorisation-des-donnees-massives.html) which is co-accredited by INP-ENSEEIHT and INSA Toulouse.

This year (2019/2020) the goal of the project is to develop a video analysis service. The main functionality is the recognition and tracking of vehicles in order to be able to estimate the emission rate (Co2) produced by traffic in the areas concerned.

# Module3_VehicleEmissions
The purpose of this module is to identify the CO2 emissions of each vehicle in road traffic.

# Interface
## Inputs
- frames_path: a string with the path where are the frames which will be used to process
- frame_contours: the list containing the bouding boxes computed bu module 2

## Output
- frames_vehicles_co2: a list of frame_vehicles_co2 objectscontaning the CO2 information for each frame

Team:
Loic Meynard
Valentin Maupin
