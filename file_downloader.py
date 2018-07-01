import requests
import sys
import time
import os
from clint.textui import progress

def downloadFile(url, directory) :
      '''Function which actually retrieves the content from
         the web. Returns the time taken for the download.
      '''

      if raw_input('Rename File? (Y or N) : ') == 'Y' :
            localFilename = raw_input('Enter Filename to save : ')
      else :
            localFilename = url.split('/')[-1] # if the user doesn't specify a new filename, use the actual one

      print 'Starting download...'
            
      r = requests.get(url, stream=True)

      start = time.clock()

      total_len = int(r.headers.get('content-length'))
      dl = 0
      
      f = open(directory + '/' + localFilename, 'wb')
      for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_len/1024) + 1) :
            if chunk :
                  dl += len(chunk)
                  
                  f.write(chunk)
                  f.flush()
                  os.fsync(f.fileno())

                  done = int(50 * dl/total_len)
      f.close()
      return (time.clock() - start)


if __name__ == '__main__' :
      if len(sys.argv) > 1 :
            url = sys.argv[1]
      else :
            url = raw_input('Enter the URL : ')

      directory = raw_input('Where would you want to save the file ? ')
      
      time_elapsed = downloadFile(url, directory)
      print 'Download complete...'
      print 'Time Elapsed: ',
      print time_elapsed,
      print 'seconds.'
      print '\n\n'
