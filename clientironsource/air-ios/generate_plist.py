#!/usr/bin/python3

import os
import sys
import time
import subprocess
import socket
import argparse
from params import *
from xml.dom.minidom import parse

def extractValueFromXML( _filename, _tag ):
    xml = parse( _filename )
    nodelist = xml.getElementsByTagName( _tag )[0]
    nameData = []
    for node in nodelist.childNodes:
        if node.nodeType == node.TEXT_NODE:
            nameData.append(node.data)
        else:
            print ( node.nodeType )
    version = ''.join(nameData)
    return version

if __name__ == "__main__":
    parser = argparse.ArgumentParser( description = 'Filling properties for plist file' )

    parser.add_argument( '--xml', default = 'application_dev.xml', help = 'AIR XML with application version' )
    parser.add_argument( '--plist_url', required = True, help = 'https url where plist will be placed' )
    parser.add_argument( '--ipa_url', required = True, help = 'http/https url of ipa file' )
    parser.add_argument( '--icon_url', required = True, help = 'http/https url of icon (png, square >= 120*120)' )
    parser.add_argument( '--title', required = True, help = 'Title shown while loading is in progress' )
    parser.add_argument( '--build_number', default = 0, help = 'Build number from CI' )

    args = parser.parse_args()

    plistTemplateFile = open( 'rats.plist.template', 'r')
    plistContent = plistTemplateFile.read()
    plistTemplateFile.close()

    plistContent = plistContent.replace( '@ipa-url', args.ipa_url )
    plistContent = plistContent.replace( '@icon-url', args.icon_url )
    plistContent = plistContent.replace( '@bundle-identifier', extractValueFromXML( args.xml, 'id' ) )
    plistContent = plistContent.replace( '@bundle-version', extractValueFromXML( args.xml, 'versionNumber' ) )
    plistContent = plistContent.replace( '@@bundle-short-version-string', extractValueFromXML( args.xml, 'versionLabel' ) + "(" + str( args.build_number ) + ")" )
    plistContent = plistContent.replace( '@title', args.title)

    plistFile = open( './dist/rats.plist', 'w' )
    plistFile.write( plistContent )

    htmlTemplateFile = open( 'ipa.html.template', 'r')
    htmlContent = htmlTemplateFile.read()
    htmlTemplateFile.close()

    htmlContent = htmlContent.replace( '@plist-url', args.plist_url )

    plistFile = open( './dist/index.html', 'w' )
    plistFile.write( htmlContent )
