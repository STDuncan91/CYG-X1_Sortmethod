import astropy.io
import astropy.io.fits
import os
import shutil

basedir = r'F:\CYG C\Cyg-X1' #Define base directory, must be nothing but .fits images

imglist = os.listdir(basedir) #Create list of base directory files for numbers and iteration

sortlist = [] #Empty sorting list
sortdir = '' #Empty sorting string
namedir = '' #Empty naming string
date = ''

for fitsimage in range(len(imglist)): #Iterate over each image
    sortlist = [] #Re-empty sorting list
    sortdir = '' #Re-empty sorting string
    hdulist = astropy.io.fits.open(basedir + '\\' + imglist[fitsimage]) #Open .fits image
    
    '''This part is important and where the meat of the sorting happens.
    You can add and remove more try-except strings to change whatever filters
    you want, but the order you try them in is going to be the order of
    sorting in the directory structure.
    
    It's important to keep them as try-except strings, as not every .fits
    image will have this data, and will throw an exception.'''
    
    try:
        sortlist.append(hdulist[0].header['TELESCOP'])
    except:
        pass
    try:
        sortlist.append(hdulist[0].header['FILTERI1'])
    except:
        pass
    try:
        sortlist.append(hdulist[0].header['FILTERI2'])
    except:
        pass
    try:
        sortlist.append(hdulist[0].header['FILTERI3'])
    except:
        pass
    try:
        sortlist.append(hdulist[0].header['FILTERI4'])
    except:
        pass
    try:
        sortlist.append(hdulist[0].header['EXPTIME'])
    except:
        pass
    try:
        date = hdulist[0].header['DATE']
    except:
        pass
    hdulist.close()
    
    for sort in range(len(sortlist)):
        sortdir = sortdir + str(sortlist[sort]) + '\\'
        
    for name in range(len(sortlist)):
        namedir = namedir + str(sortlist[name]) + ' '
    
    if not os.path.exists(basedir + '\\' + sortdir):
        os.makedirs(basedir + '\\' + sortdir)
    shutil.move(basedir + '\\' + imglist[fitsimage], basedir + '\\' + sortdir + 'CYG-X1 ' + date + ' ' + namedir)
