import sys

if len(sys.argv) < 2:
   print("No file path given")
   exit()

sourceFile = open(sys.argv[1], "r")
sourceCode = sourceFile .read()

finalFile = open("test.gcode", "w")
finalCode = ""

sourceCode = sourceCode.splitlines()

x_axes = 1.0
z_hight = 0

for line in sourceCode:
   if(line[0:3] == ";Z:"):
      finalFile.write(line)
      finalFile.write('\n')
      z_hight = line[3:]
      continue

   if(line == "M600"):
      finalFile.write('\n')
      finalFile.write(';added gcode' + '\n')
      finalFile.write('G1 X' + str(x_axes) + ' Y10.0 F9000' + '\n')
      finalFile.write(line + '\n')
      finalFile.write('G1 Z0.20' + '\n')
      finalFile.write('G1 X' + str(x_axes) + ' Y140 E10 F1500' + '\n')
      x_axes += 0.3
      finalFile.write('G1 X' + str(x_axes) + ' Y140' + '\n')
      x_axes += 0.7
      finalFile.write('G1 Z' + str(z_hight) + '\n')
      finalFile.write('\n')
      continue
      

   finalFile.write(line + '\n')


finalFile.close()
sourceFile .close()