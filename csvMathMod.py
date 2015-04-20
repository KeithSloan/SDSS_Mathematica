import sys, os

# Path for temporary transfer files
prefix = "/ram/"
# filename lead in for transfer files
xfer = "xfer-"

def csv2math(lines):

    striped_lines = []
    for line in lines:
        foo = line.strip('\n\r #')
        striped_lines.append(foo)
    print striped_lines

    data = []
    for line in lines[1:]:
        data.append(line[:-1].split(','))

    rp = open(prefix+"Results", "w")
    vp = open(prefix+"Vars","w")
 
    for col in striped_lines[:1] :
#        print col
        cc = col.split(',')
        x = 0
        for nn in cc:
# underscores not allowed in Mathematica Variables
	    mm = nn.replace('_','')
# Mathematica Variables must start with a lower case
	    nn=mm[:1].lower() + mm[1:]
            print nn
            if ( x > 0 ) : vp.write(",") 
            vp.write(nn) 
            rp.write(nn+'= ReadList["'+prefix+xfer+nn+'"]\n')
            fp = open(prefix+xfer+nn, 'w') 
            y = 0
            for z in data:
#               print data[y][x] 
                fp.write(data[y][x]+"\n")
                y = y + 1
#            fp.write('\n')
            fp.close()
            x = x + 1
    rp.close()
    vp.close()
    print('Now execute in Mathematica : Get ["'+prefix+'Results"]\n')
