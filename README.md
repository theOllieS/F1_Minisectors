# F1_Minisectors


**** I am very inexperienced at coding and I apologize in advance for the messy scripts ****

**** If you find any ways to imporve this method please let me know as I would love to make it as good and as functional as it can be ****



This is a very basic method to plot the circuit map with a defined integer number of minisectors.

This is not corresponding to the minisectors that may show on the F1 app. My method divides the circuit up into equal length minisectors, the drivers in these sectors are then ranked in terms of highest average speed during each sector, and then plotting the minisector in the colour of the fastest driver with the added ability to label with the driver's number. 

I have used a quicklaps threshold (usually about 103% of the best time in the session) which allows for more reliable data collection. This is because the fastf1 get_telemetry() function can return errors for certian slower laps if not used. 

At present the minisectors script takes the drivers' best laptime from the session, with the added option to limit it to the drivers best lap in Q3. 

I have used custom colour schemes that I have used along side the fastf1 package. You are welcome to import these or use alternatives. 

My ultimate goal for this would for it to be a callable function with the driver numbers' as toggleable (on/off) labels built in to the function. 



I would like to credit @jaspervhat on medium.com for the inspiration of the method to divide the circuit into minisectors; see this link https://medium.com/towards-formula-1-analysis/formula-1-data-analysis-tutorial-2021-russian-gp-to-box-or-not-to-box-da6399bd4a39; and of course @theOehrly brilliant fastf1 package https://github.com/theOehrly/Fast-F1. 
