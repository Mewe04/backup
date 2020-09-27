import os, time, sys, zipfile


blacklist = [
    '/proc',
    '/dev',
    '/etc'
]


def backup(time, filess):
    try:
        os.mkdir('{0}'.format(time))
        zipchik = zipfile.ZipFile('{0}/Backup {1}.zip'.format(time, time), 'w')
        for folder, subfolders, files in os.walk(filess):
            for file in files:
                zipchik.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), filess), compress_type = zipfile.ZIP_DEFLATED)
        zipchik.close()
        return 'Backup completed successfully!'
    except:
        print('Oh! An unexpected error has occurred!')
        pass


try:
    if len(sys.argv) > 2:
        print('More than two arguments entered')
    elif len(sys.argv) == 1:
        print('Please specify the file you want to back up\n\nFor example:\n   python3 backup.py file\n   (Use sudo if required)')
    elif sys.argv[1] in blacklist:
        print('Oh! An unexpected error has occurred!')
    else:
        backup(time.strftime('%H:%M %m.%d.%Y', time.localtime()), sys.argv[1])
except:
    print('Oh! An unexpected error has occurred!')
    pass

