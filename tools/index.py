#!/usr/bin/env python3
#  CAN-FIX Data Distribution System
#  Copyright (c) 2023 Phil Birkelbach
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

# This program is used to generate the index.  The index file itself should
# not be edited manually.

import json
import datetime
import os
import hashlib

index_file = "../index/cfdataindex.json"

# First we'll deal with the header information in the file...


output = {} # This is the main dictionary that will become the index file

output['name'] = "CAN-FiX Data Distribution Index"
output['version'] = 1.0
output['updated'] = datetime.datetime.utcnow().isoformat()

eds = []
output['eds_index'] = eds

# We'll start out by loading the eds files that we keep here on the
# github repo.

eds_path = "../data/eds"
dirlist = os.listdir("../data/eds")
baseuri = "https://raw.githubusercontent.com/birkelbach/canfix-data/master/data/eds/"

for filename in dirlist:
    if filename[-5:] == ".json":
        with open(f"{eds_path}/" + filename) as json_file:
            print(f"Loading device file {filename}")
            d = json.load(json_file)
            json_file.seek(0)
            sha = hashlib.sha256()
            while True:
                data = json_file.read(65536)
                if not data:
                    break
                sha.update(data.encode())
    else:
        raise Exception("Oh Heck No")

    # These four values define an individual type of device that this eds would apply to
    dd = {"name":d['name'],"type":d['type'],"model":d['model'],"version":d['version']}
    t = os.path.getmtime(f"{eds_path}/" + filename)
    
    dd["modified"] = datetime.datetime.fromtimestamp(t).isoformat()
    dd["sha256"] = sha.hexdigest()
    dd["filename"] = filename # We will have to make sure that these are unique
    dd["uri"] = baseuri + filename
    eds.append(dd)
    

# Since the only files that we know about are these we'll stop here 

# For eds files not located here we could have a simple list that would need
# to be maintained.  This would probably work for simple devices that are not
# updated very often.

# Another method will probably be to have a list of URIs that would have yet
# other indexes that could be maintained by those people.  When this script
# is run it would read those indexes and put that information in this file



#print(json.dumps(output, indent=2))
with open(index_file, 'w') as file:
    json.dump(output, file, indent=2)

