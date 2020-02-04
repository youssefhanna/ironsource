#!/usr/bin/python3

import os
import re

if __name__ == "__main__":
    revisionTag = "Rev:"
    fileCompileInfo = os.path.normpath( 'bin/client_compile_info' )
    fileVersionInfo = os.path.normpath( 'bin/client_version_info' )

    if os.path.exists( fileVersionInfo ):
        os.remove( fileVersionInfo )

    if os.path.exists( fileCompileInfo ):
      for line in open( fileCompileInfo, "r" ):
        if re.match( revisionTag, line ):
          with open( fileVersionInfo, "w" ) as file:
            rx = re.compile( "^"+revisionTag+"\s*(\d*)" )
            file.write( rx.search( line ).groups()[0] )
          break
      os.remove( fileCompileInfo )
