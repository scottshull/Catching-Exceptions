try:
    with open("Myfile.txt", 'r+') as f:
        line = f.readlines()
except IOError as e:
    print "File not found({0}) : {1}".format(e.errno, e.strerror)
print "\n\n"

while True:
    try:
        t = int(raw_input("Enter a number: \n"))
        break
    except ValueError:
        print "Your input was not valid. Try again \n"
