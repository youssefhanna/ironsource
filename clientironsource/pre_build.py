#!/usr/bin/python3

import os
import sys
import time
import subprocess

def getSvnInfoDict( _workDir ):
    versionstr = "1.0"
    arr = versionstr.splitlines()
    values = {}
    for line in arr:
        rec = line.split( ":", 1 )
        if len(rec) < 2:
            continue
        values[rec[0].strip()] = rec[1].strip()
    return values

def getSvnRevision( _workDir ):
    rev = subprocess.check_output( ["svnversion", _workDir, "-n"] ).decode().strip()
    return rev

def makeCompileInfo( _workDir ):
    buildDate = time.strftime("%d.%m.%Y")
    buildTime = time.strftime("%H:%M")
    rev = getSvnRevision( _workDir )
    tag = getSvnInfoDict( _workDir ).get( 'Relative URL' )
    clientInfo = "Build Time: {0} {1}\nRev: {2}\nTag: {3}".format( buildDate, buildTime, rev, tag )
    return clientInfo

if __name__ == "__main__":
    numargs = len ( sys.argv )

    if (numargs == 2):
      pathRoot = sys.argv[1]
    else:
      print ( 'wrong input params' )
      exit(1)

    fileVersionInfo = os.path.normpath( 'bin/client_version_info' )
    if os.path.exists( fileVersionInfo ):
        os.remove( fileVersionInfo )

    workDir = os.path.normpath( sys.argv[1] )
    compileInfo = makeCompileInfo( workDir )

    outputCompileInfo = os.path.join( workDir, os.path.normpath( 'bin/client_compile_info' ))
    with open( outputCompileInfo, "w") as file:
      file.write( compileInfo )

