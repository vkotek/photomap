# photomap
AWS app that takes photos as input and plots them on a geographical map.


PS: There seems to be a bug in the exifread library, causing import to fail when module is imported locally from a subfolder. The bug is resolved by changing the import statement from "from exifread.utils" to "from ...utils". This is found in exifread/tags/markernote/fujifilm.py". 
