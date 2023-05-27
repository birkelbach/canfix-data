============
Introduction
============

FIX is an acronym for Flight Information eXchange.  It is a set of protocol
specifications for exchanging information between aircraft avionics and flight
systems.  This specification and the protocols themselves are licensed under a
Creative Commons license that allows anyone to modify and redistribute these
documents without charge.

This is a community supported endeavor, with the primary goal of providing a
standard method for avionics and flight control systems to communicate with one
other in a vendor neutral way.


General Description
-------------------

The goal of this project is to create a standardized way in which data files
can be distributed to the FIX ecosystem.  This began as a need to get Electronic
Data Sheets (EDS Files) to the CAN-FiX Configuration Utility.  These EDS files 
describe the node to the Utility so one program can be used to configure any
node that supplies an EDS.

As time goes on there may be additional needs for data that would need to be
kept up to date.  This project should be able to expand to fill those needs
as well.

The basic idea is to maintain one or more index files at a location that
is publicly available.  Software that would need this data would simply
need to access the proper index file and the locations of the specific data
files would be specified in the index.

We don't expect this index to be terribly large so for the time being we
will create a simple JSON file that can be downloaded and parsed.

A description of how this JSON file should be structured will follow.

