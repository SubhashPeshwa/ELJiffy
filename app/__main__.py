from .model.azure.auth import AuthService
from .model.azure.blob import BlobService
import asyncio

copy_from_container =""
copy_to_container =""
blob_name =""
blob_url = ""


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

authService = AuthService()
credential = authService.managed_identity()
# credential = authService.vs_code()

blobService = BlobService(credential,copy_from_container, copy_to_container, blob_name, blob_url)
blob = loop.run_until_complete(blobService.get_blob())

loop.close()