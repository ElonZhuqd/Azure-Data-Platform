# Databricks notebook source
storageAccountName = "adlsdev"
# Create Databricks Secret Scope and assign Key Vault DNS and Resource ID under KV property
storageAccountAccessKey = dbutils.secrets.get('kv-scope-dev', 'adls-access-key-dev')
mountPoints=["gold","silver","bronze","landing","configs"]
for mountPoint in mountPoints:
    if not any(mount.mountPoint == f"/mnt/{mountPoint}" for mount in dbutils.fs.mounts()):
        try:
            dbutils.fs.mount(
            source = "wasbs://{}@{}.blob.core.windows.net".format(mountPoint, storageAccountName),
            mount_point = f"/mnt/{mountPoint}",
            extra_configs = {'fs.azure.account.key.' + storageAccountName + '.blob.core.windows.net': storageAccountAccessKey}
            )
            print(f"{mountPoint} mount succeeded!")
        except Exception as e:
            print("mount exception", e)

dbutils.fs.mounts()