#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dexnet
from dexnet.database.mesh_processor import MeshProcessor

dexnet_api = dexnet.DexNet()
dexnet_api.open_database('/media/ai/New Volume/AAAA.hdf5', create_db=False)
dexnet_api.open_dataset('DS-3')

listObjs = dexnet_api.list_objects()
for i in range(0, len(listObjs)):
    print("new Name :", listObjs[i])
    print("number :",  i)
    try:
        dexnet_api.display_stable_poses(listObjs[i])
    except Exception as e:
        print ("No stable Poses")
        print("Name :", listObjs[i])
        print("number :",  i)
        print ("No stable Poses")
        print("Name :", listObjs[i])
        print("number :",  i)
        print ("No stable Poses")
        continue

dexnet_api.close_database()


