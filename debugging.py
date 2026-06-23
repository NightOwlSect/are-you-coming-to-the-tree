# debugging example courtesy of LaunchCode education

launchReady = False
fuelLevel = 17000

if fuel_Level >= 20000:
   print('Fuel level cleared.')
   launchReady = True
else:
   print('WARNING: Insufficient fuel!')
   launchReady = False

crewStatus = true
computerStatus = 'green'

if crewStatus and computerStatus == 'green':
   print('Crew & computer cleared.')
   launchReady = True
else:
   print('WARNING: Crew or computer not ready!')
   launchReady = False

if (launchReady):
   print(("10, 9, 8, 7, 6, 5, 4, 3, 2, 1...")
   print("Ignition...")
   print("Liftoff!")
else:
   print("Launch scrubbed.")
