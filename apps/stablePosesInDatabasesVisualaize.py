#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dexnet
from dexnet.database.mesh_processor import MeshProcessor

dexnet_api = dexnet.DexNet()
dexnet_api.open_database('/media/ai/1CDDFB7F5EC6C007/300-ABC-sample-test.hdf5', create_db=False)
dexnet_api.open_dataset('X-min-05')
todeleteobjs = []
listObjs = dexnet_api.list_objects()
for i in range(65, len(listObjs)):
    print("new Name :", listObjs[i])
    print("number :",  i)
    try:
        #dexnet_api.display_stable_poses(listObjs[i])
        stablePoses = dexnet_api.dataset.stable_poses(listObjs[i])
    except Exception as e:
        print ("No stable Poses")
        print("Name :", listObjs[i])
        print("number :",  i)
        #print ("No stable Poses")
        #print("Name :", listObjs[i])
        #print("number :",  i)
        #print ("No stable Poses")
        #dexnet_api.delete_object(listObjs[i])
        todeleteobjs.append(str(listObjs[i]))
        continue

dexnet_api.close_database()
print(todeleteobjs)

