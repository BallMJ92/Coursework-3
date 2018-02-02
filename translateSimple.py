def main() :
   transMap = buildMapping("textabbv.txt")
   print("Enter a message to be translated:")
   message = input("")

   translation = message
   for k in transMap :
      translation = translation.replace(transMap[k], k)
   print(translation)
      
def buildMapping(filename) :
   transMap = {}
   infile = open(filename, "r")
   for line in infile:
      parts = line.split(":")
      transMap[parts[0]] = parts[1].rstrip()
   infile.close()
   return transMap
main()
