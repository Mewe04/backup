import os
import sys
import time
import zipfile

blacklist = [
    '/proc',
    '/dev',
    '/etc'
]


def backup(times, filess):
    os.mkdir('{0}'.format(times))
    zipchik = zipfile.ZipFile('{0}/Backup {1}.zip'.format(times, times), 'w')
    for folder, subfolders, files in os.walk(filess):
        for file in files:
            zipchik.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), filess),
                          compress_type=zipfile.ZIP_DEFLATED)
    zipchik.close()
    return 'Backup completed successfully!'


if len(sys.argv) > 2:
    print('More than two arguments entered')
elif len(sys.argv) == 1:
    print(
        'Please specify the file you want to back up\n\nFor example:\n   python3 backup.py file\n   (Use sudo if '
        'required)')
elif sys.argv[1] in blacklist:
    print('Oh! An unexpected error has occurred!')
else:
    backup(time.strftime('%H:%M %m.%d.%Y', time.localtime()), sys.argv[1])
